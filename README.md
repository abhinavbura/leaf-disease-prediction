
# leaf-disease-prediction

This project aims to predict leaf diseases by analyzing the area of the leaf that is diseased, the percentage of the area damaged, and determining whether the infection is caused by a fungus or a virus. The project uses VGG19, ResNet50, a hybrid model of these two architectures, and YOLOv5 for diseased area prediction.




## Features

- Detection of diseased area on leaf images using YOLOv5
- Calculation of the percentage of the area damaged
- Classification of the disease as a fungal or viral infection



## Technologies Used

- Python
- Python
- TensorFlow/Keras
- OpenCV
- NumPy
- Matplotlib
- YOLOv5


## Model Architectures
**VGG19**\
VGG19 is a convolutional neural network architecture that uses 19 layers. It is known for its simplicity and effectiveness in image classification tasks.

**ResNet50**\
ResNet50 is a 50-layer deep convolutional neural network. It introduces residual connections to solve the vanishing gradient problem, allowing for the training of very deep networks.

**Hybrid Model**\
The hybrid model combines features from both VGG19 and ResNet50 to leverage the strengths of both architectures. This model aims to improve the accuracy and robustness of leaf disease predictions.

**YOLOv5**\
YOLOv5 (You Only Look Once) is an object detection model that predicts bounding boxes around diseased areas of leaves. It is known for its speed and accuracy in object detection tasks.
## Results
The models were evaluated on a test set, and the hybrid model achieved the best performance. Here are some key metrics:\
(results obatined on 3 epochs)
- VGG19 Accuracy: 54%
- ResNet50 Accuracy: 52%
- Hybrid Model Accuracy: 68%

## Installation

Install my-project with npm
1. Clone the repository
```bash
  git clone https://github.com/abhinavbura/leaf-disease-prediction.git
```
2. Navigate to the project directory:
```bash
  cd leaf-disease-prediction
```
3. Create and activate a virtual environment:
```bash
  python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
```
4. Install the required dependencies:
```bash
  pip install -r requirements.txt
```
5. Open Jupyter Notebook and run the cells.
