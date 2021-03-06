#!/home/dh_nfjxcr/artishan.io/venv/bin/python3

from PIL import Image
import torch as th
import json
import time 
import os 

from app import app
from logging import WARNING

from glide_text2im.download import load_checkpoint
from glide_text2im.model_creation import (
    create_model_and_diffusion,
    model_and_diffusion_defaults,
    model_and_diffusion_defaults_upsampler
    
    
)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(APP_ROOT, 'base.pt')


# This notebook supports both CPU and GPU.
# On CPU, generating one sample may take on the order of 20 minutes.
# On a GPU, it should be under a minute.
has_cuda = th.cuda.is_available()
device = th.device('cpu' if not has_cuda else 'cuda')

# Create base model.
options = model_and_diffusion_defaults()
options['use_fp16'] = has_cuda
options['timestep_respacing'] = '2' # use 100 diffusion steps for fast sampling
model, diffusion = create_model_and_diffusion(**options)
if has_cuda:
    model.convert_to_fp16()

model.to(device)

#name = checkpoint.__class__.__name__
#app.logger.warning("Checkpoint name:  " + name)




batch_size = 1
guidance_scale = 3.0
upsample_temp = 0.1
full_batch_size = batch_size * 2

def makemodel():
    
    checkpoint = th.load(PATH)
    model.load_state_dict(checkpoint, device)
    model.eval()
    
    #print('total base parameters', sum(x.numel() for x in model.parameters()))
    
    


def show_images(batch: th.Tensor):
    """ Display a batch of images inline. """
    scaled = ((batch + 1)*127.5).round().clamp(0,255).to(th.uint8).cpu()
    reshaped = scaled.permute(2, 0, 3, 1).reshape([batch.shape[2], -1, 3])
    image = Image.fromarray(reshaped.numpy())
    return image

def requestimage(prompt_text):
    makemodel()
    print("model made")
    # Sampling parameters
    prompt = "Dog"

    # Tune this parameter to control the sharpness of 256x256 images.
    # A value of 1.0 is sharper, but sometimes results in grainy artifacts.

    ##############################
    # Sample from the base model #
    ##############################

    # Create the text tokens to feed to the model.
    tokens = model.tokenizer.encode(prompt)
    tokens, mask = model.tokenizer.padded_tokens_and_mask(
        tokens, options['text_ctx']
    )

    # Create the classifier-free guidance tokens (empty)
    #full_batch_size = batch_size * 2
    uncond_tokens, uncond_mask = model.tokenizer.padded_tokens_and_mask(
        [], options['text_ctx']
    )

    # Pack the tokens together into model kwargs.
    model_kwargs = dict(
        tokens=th.tensor(
            [tokens] * batch_size + [uncond_tokens] * batch_size, device=device
        ),
        mask=th.tensor(
            [mask] * batch_size + [uncond_mask] * batch_size,
            dtype=th.bool,
            device=device,
        ),
    )
    img = sample_model(model_kwargs)

    return img

# Create a classifier-free guidance sampling function
def model_fn(x_t, ts, **kwargs):
    half = x_t[: len(x_t) // 2]
    combined = th.cat([half, half], dim=0)
    model_out = model(combined, ts, **kwargs)
    eps, rest = model_out[:, :3], model_out[:, 3:]
    cond_eps, uncond_eps = th.split(eps, len(eps) // 2, dim=0)
    half_eps = uncond_eps + guidance_scale * (cond_eps - uncond_eps)
    eps = th.cat([half_eps, half_eps], dim=0)
    return th.cat([eps, rest], dim=1)

# Sample from the base model.
def sample_model(kwargs):
    model.del_cache()
    samples = diffusion.p_sample_loop(
        model_fn,
        (full_batch_size, 3, options["image_size"], options["image_size"]),
        device=device,
        clip_denoised=True,
        progress=True,
        model_kwargs=kwargs,
        cond_fn=None,
    )[:batch_size]
    model.del_cache()
    return show_images(samples)


