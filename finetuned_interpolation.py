from finetuned.corridor import corridor_interpolation
from finetuned.sphere import sphere_interpolation


# Corridor dataset interpolation
corridor_interpolation(model_path='./flownet2/pretrained_models/FlowNet2_checkpoint.pth.tar')

# Sphere dataset interpolation
sphere_interpolation(model_path='./flownet2/pretrained_models/FlowNet2_checkpoint.pth.tar')
