# RDVSv2: A Large-scale Benchmark for RGB-D Video Salient Object Detection

This README is about reproducing the paper [RDVSv2: A Large-scale Benchmark for RGB-D Video Salient Object Detection]().

## Table of Contents
- [Downloads](#downloads)
- [Supplementary Material](#supplementary-material)
---

## Downloads
### RDVSv2 Dataset

The full dataset (including RGB video URLs, depth maps, optical flow maps, and ground truth annotations) together with the heatmaps can be downloaded from:  
- [Google Drive](https://drive.google.com/drive/folders/1aB0Mq7I6Un37miT0LYkRgn7xr3vA44lx?usp=drive_link)  
- [Baidu Pan](https://pan.baidu.com/s/1ou80dz5CsEKN6A96dqUgQA?pwd=kfsy) (Extraction code: `kfsy`)(The complete dataset, including the RGB frames, is also available at this link, in the RDVSv2_RGB folder. If there is any infringement, please contact us to have it removed.)

Use the data split tool in the [`datasetScript`](./datasetScript) folder to download the videos and split them into frames.

## Supplementary Material
Supplementary material for ACM Multimedia 2026 Dataset Track review is available in [`SUPPLEMENTARY.md`](SUPPLEMENTARY.md).

## License

The source code and configuration files in this repository are
licensed under the [Apache License 2.0](LICENSE).

The annotations, segmentation masks, dataset splits, metadata, and
other dataset components created by the RDVSv2 authors are licensed
under the [Creative Commons Attribution-NonCommercial 4.0
International License (CC BY-NC 4.0)](DATA_LICENSE.md).

Commercial use of the licensed dataset components requires separate
prior written permission from the RDVSv2 rights holders.
