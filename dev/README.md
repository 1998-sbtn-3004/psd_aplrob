# Models \& Training
## Model Architectures

- **[YOLOv8](https://yolov8.com/) (You Only Look Once, latest Ultra version)**: Modern, fast, and highly accurate real-time object detection architecture. It excels in aerial and real-world scenes and supports fine-tuning for specific classes like "free," "occupied," and "unknown" parking spots. YOLO also has strong community support and many tutorials for custom dataset training.
- **[Detectron2 (by Facebook AI)](https://github.com/facebookresearch/detectron2)**: State-of-the-art instance segmentation framework. It is ideal if you want pixel-level segmentation, which can delineate irregular parking spaces rather than just bounding boxes. It is more resource-intensive but provides very high accuracy for complex images like parking lots.
- **[MMDetection](https://github.com/open-mmlab/mmdetection)**: Flexible open-source toolbox that supports a range of object detection algorithms including RetinaNet, Faster R-CNN, and Cascade R-CNN. Useful if you want to experiment or compare different detectors.

| Model | Detection Type | Real-Time Suitable | Community/Tutorials | Integration Difficulty |
| :-- | :-- | :-- | :-- | :-- |
| YOLOv8 | Bounding boxes | Yes | Excellent | Low-Medium |
| Detectron2 | Instance Segmentation | No (slower) | Good | Medium-High |
| MMDetection | Both | Varies | Good | Medium |

## Training \& Labeling Strategy

Labeling is foundational:

- **Bounding Boxes:** Each parking spot is labeled with a rectangle and assigned a class (free, occupied, unknown). This works well for YOLO and standard object detectors.
- **Segmentation Masks:** Each parking space is segmented (drawn with a polygon around its outline). This is essential for Detectron2 and pixel-precise needs.

### Labeling Tools

- [LabelImg](https://github.com/tzutalin/labelImg) – Free, easy, for bounding boxes (YOLO, Pascal VOC).
- [CVAT](https://cvat.ai) – Robust, web-based; supports bounding box, segmentation, and team collaboration.
- [Supervisely](https://supervise.ly) – Cloud-based, rich format support, advanced polygon and tagging tools.

**Recommended Workflow:**

1. **Capture diverse aerial images** under different light, weather, and occupancy conditions. ✅ (Partially done, but not enough images)
2. **Draw boxes or segment each parking space** and label them as ‘free’, ‘occupied’, or 'unknown'. (see Notios Board for more details of tasks)
3. **Export labels in a format compatible with your chosen model** (YOLO format is most common and easy to use).
4. **Augment your dataset** (flip images, hue shift, brightness, random crop) to increase model robustness. (Use python script)
5. **Split images into train/validation/test sets** (commonly 80/10/10). (use python script)

## Evaluation of Approaches

### YOLO-based Detection

- **Pros:** Real-time inference, easy to set up, highly accurate for parking spots in overhead views, plenty of documentation.
- **Cons:** Bounding boxes may not fit irregularly shaped spots perfectly; confusion can occur in tight or crowded lots. (Not as important for our use-case, might be the case when nearly all spots are taken or drivers parked weird—not in between the markings)


### Instance Segmentation (Detectron2)

- **Pros:** Precise outlines of parking spaces, better in complex and non-standard layouts. (Not necessary for our use-case)
- **Cons:** Labeling is time-intensive; training and inference require more GPU resources; not strictly real time.

Conclusion: YOLO is the best option for our use-case.


### Model Training

- **Transfer learning** is strongly advised—start from weights pre-trained on COCO or similar datasets and fine-tune with your own labeled data. This dramatically reduces the amount of data/time required to achieve strong results.


### Labeling Details / Tips

- Quality is crucial—ambiguous or incorrectly labeled boxes/polygons will reduce system reliability
- **Avoid overlapping boxes** (e.g. two parking spots in the same image)
- Label each parking spot in detail

## Problem Fields
- (How) do we detect special parking spots, i.e. handicapped parking space, reservered parking spaces and so on ? 

## Conclusion

For a university project aiming for a web app with live feedback:

- **[YOLOv8](https://yolov8.com/)** is the best balance of speed, accuracy, and ease of use for drone view object detection — **unless** we specifically need pixel-level edges.
- We should use **[LabelImg](https://github.com/tzutalin/labelImg)** for quick start, instead of using **CVAT** or **Supervisely**, which are used for advanced/segmentation annotation or larger teams.

---
