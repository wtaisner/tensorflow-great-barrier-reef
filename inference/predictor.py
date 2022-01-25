import torch
import torchvision
import numpy as np
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from torchvision.io import read_image, write_png


def slice_output(output: dict, confidence_threshold: float = 0.5) -> dict:
    """
    this method is responsible for validating models output w.r.t confidence_threshold defined above.
    It accepts an output dictionary from model, namely {'boxes':[], 'labels':[], 'scores':[]}
    It returns a dictionary sliced to items with score above confidence_threshold
    """

    num_valid_elements = np.sum(np.array(output['scores'].detach().numpy()) >= confidence_threshold)
    if num_valid_elements == 0:
        num_valid_elements = 1
    res = {}
    for key, value in output.items():
        res[key] = value[:num_valid_elements]
    return res


num_classes = 2  #

model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained_backbone=False)
in_features = model.roi_heads.box_predictor.cls_score.in_features
model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

# load trained model
model.load_state_dict(torch.load('models/FastRCNN-Adam.pt', map_location=torch.device('cpu')))

model.eval()

test_image = read_image('test_data/test_image.jpg')
img = test_image.detach().clone()
min_image = img.min()
max_image = img.max()
# normalize image to 0-1 - required by torchvision
img -= min_image
img = torch.FloatTensor(img / max_image)
img = torch.unsqueeze(img, 0)

output = model(img)
output = slice_output(output[0])
colors = ['red' for _ in range(len(output['boxes']))]
result = torchvision.utils.draw_bounding_boxes(test_image, output['boxes'], colors=colors, width=5)
write_png(result, filename='result_image.png')
