# Supplementary Material for RDVSv2: A Large-scale Benchmark for RGB-D Video Salient Object Detection

This document provides additional details about the paper [RDVSv2: A Large-scale Benchmark for RGB-D Video Salient Object Detection]().

## Table of Contents
- [Dataset Annotation](#dataset-annotation)
- [Further Dataset Description and Analysis](#further-dataset-description-and-analysis)
- [Dataset Training/Testing Splits](#dataset-trainingtesting-splits)
- [Quantitative Results](#quantitative-results)
- [Ablation Study](#ablation-study)
---

## Dataset Annotation

Following the eye-tracking-based annotation paradigm established in prior studies [[1]](#ref1)–[[3]](#ref3), we collect gaze data from participants during free viewing of video stimuli using a Tobii Eye Tracker 4C. The experimental setup follows prior protocols: the eye tracker operates at 90 Hz, and the stimuli are displayed on a 23.8-inch monitor with a resolution of 1920 × 1080. A chinrest is used to minimize head movement, and the viewing distance is maintained at approximately 70 cm throughout the experiment.

To improve the robustness and generalizability of the annotations, we expand the participant pool to 22 eligible subjects (14 male and 8 female, aged 22 to 35). All participants successfully complete the eye-tracker calibration procedure, have normal or corrected-to-normal vision, and have no prior exposure to the video materials. During the experiment, only RGB video frames are presented to the participants, while depth information is intentionally withheld to avoid biasing visual attention, following the annotation protocols adopted by existing RGB-D SOD datasets [[4]](#ref4)–[[6]](#ref6).

The collected gaze points from all participants are processed using a Gaussian filter to generate continuous fixation saliency heatmaps, which are used to guide the annotation of salient object masks. To efficiently support annotation at this scale, we adopt a semi-automatic pipeline instead of relying entirely on manual labeling. Specifically, trained annotators first identify the primary salient objects in each frame with reference to the fixation heatmaps. SAM2 [[12]](#ref12) is then employed to generate initial segmentation results for these candidate regions, after which the annotators carefully refine the predicted boundaries to obtain accurate object masks. This hybrid strategy substantially improves annotation efficiency while preserving fine-grained annotation quality. Because the annotations are grounded in real gaze data, the resulting dataset naturally captures dynamic saliency transitions, where the salient object may vary over time, a property also observed in datasets such as DAVSOD [[1]](#ref1).

## Further Dataset Description and Analysis

### Description of Attributes

| Att. | Description |
|------|-------------|
| HO   | *Heterogeneous Object*. Object regions have distinct colors. |
| OCC  | *Occlusion*. Object becomes partially or fully occluded. |
| OV   | *Out-of-view*. Object is partially clipped by the image boundaries. |
| FM   | *Fast-Motion*. The average per-frame object motion, computed as centroids Euclidean distance, is larger than 20 pixels. |
| MB   | *Motion Blur*. Object has fuzzy boundaries due to fast motion. |
| DEF  | *Deformation*. Object presents complex non-rigid deformations. |
| SC   | *Shape Complexity*. Object has complex boundaries such as thin parts and holes. |
| SV   | *Scale-Variation*. The area ratio among any pair of bounding boxes enclosing the target object is smaller than 0.5. |
| AC   | *Appearance Change*. Noticeable appearance variation, due to illumination changes and relative camera-object rotation. |
| BC   | *Background Clutter*. The background and foreground regions around object boundaries have similar colors. |
| BO   | *Big Object*. Ratio of object and image areas becomes larger than 0.25. |
| SO   | *Small Object*. Ratio of object and image areas becomes less than 0.01. |
| IN   | *Indoor Scenes*. Objects are captured in indoor environment. |
| OUT  | *Outdoor Scenes*. Objects are captured in outdoor environment. |
| --- | --- |
| SH   | *Shift*. Attention shifts occur between salient objects. |
| MO   | *Multiple Objects*. There are multiple salient objects. |

**Table 1:** List of video attributes and the corresponding description. We refer to [[3]](#ref3), [[7]](#ref7) and extend a part of their attributes (top) with two additional general attributes (bottom).

### Object Size Distribution

<a id="fig1"></a>
<div align="center">
  <img src="./figs/combined_statistics_final.png" width="50%">
  <p style="text-align: center;"><b>Fig. 1</b></p>
</div>

[Fig. 1](#fig1) illustrates the distribution of normalized salient object size, defined as the ratio of the salient object's pixel area to the total frame area. Compared with other RGB-D VSOD datasets, whose object size ratios are heavily concentrated below 0.3, RDVSv2 contains a relatively smaller proportion of extremely small salient objects. In addition, a secondary peak appears around 0.5 in the distribution of RDVSv2, indicating that salient objects in our dataset are generally larger in scale. This distributional shift enriches the training data and helps alleviate the under-representation of medium-to-large salient objects in existing datasets.

### Frame Count Comparison

<a id="fig2"></a>
<div align="center">
    <img src="./figs/frame_count_comparison.png" width="50%" />
    <p style="text-align: center;"><b>Fig. 2</b></p>
</div> 

We also compile statistics on the distributions of video sequence lengths and salient object size ratios in RDVSv2, together with those of other RGB-D VSOD datasets. [Fig. 2](#fig2) presents the distribution of sequence lengths. DViSal [[8]](#ref8) is excluded from this comparison because it lacks per-frame annotations and generally contains excessively long sequences. The results show that RDVSv2 covers a substantially broader range of frame counts. Specifically, RDVS [[3]](#ref3) contains a high proportion of sequences with fewer than 100 frames, whereas the sequences in ViDSOD-100 [[9]](#ref9) are mainly concentrated around 100 frames. By contrast, RDVSv2 includes a considerably larger proportion of longer videos. This property provides more diverse training samples, making RDVSv2 particularly suitable for developing models that require long-term temporal modeling.

## Dataset Training/Testing Splits

<div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
  <a id="fig3"></a>
  <div align="center">
    <img src="./figs/data_split_1.png" width="50%" />
    <p style="text-align: center;"><b>Fig. 3</b></p>
  </div>
  <a id="fig4"></a>
  <div align="center">
    <img src="./figs/data_split_2.png" width="50%" />
    <p style="text-align: center;"><b>Fig. 4</b></p>
  </div>
</div>

As shown in [Fig. 3](#fig3) and [Fig. 4](#fig4), the quantities of object categories and attributes are partitioned into training and test sets following an approximate 7:3 ratio.

## Quantitative Results
### Qualitative Comparison on RDVSv2 Test Set after Fine-tuning.

<a id="fig5"></a>
<div align="center">
  <img src="./figs/qe1.png" width="50%">
  <p style="text-align: center;"><b>Fig. 5</b></p>
</div>

For qualitative evaluation, in [Fig. 5](#fig5), we present a qualitative comparison of our method against three other state-of-the-art (SOTA) models (DCTNet [[10]](#ref10), DCTNet+ [[3]](#ref3), and SAM-DAQ [[11]](#ref11)), all fine-tuned on the RDVSv2 training set and evaluated on its test set. It can be observed that our method achieves superior performance in salient object identification and segmentation, particularly for large objects.

### Quantitative Comparison with SOTA Methods.

<a id="fig6"></a>
<div align="center">
  <img src="./figs/qe2.png" width="50%">
  <p style="text-align: center;"><b>Fig. 6</b></p>
</div>

The quantitative results on the three RGB-D VSOD datasets are shown in [Fig. 6](#fig6). As can be observed, our model also achieves superiority in both salient object identification and the quality of salient object segmentation.

## Ablation Study

<a id="fig7"></a>
<div align="center">
  <img src="./figs/ablation_study.png" width="50%">
  <p style="text-align: center;"><b>Table 2: Ablation study on RDVS <a href="#ref3">[3]</b></p>
</div>

We conduct two ablation studies. Since prior SAM2-based methods use only RGB and depth modalities without incorporating optical flow, we first examine whether the superiority of our model comes solely from the additional motion modality. To this end, we adapt our model to use only RGB and depth as input (denoted as B1) and compare it with two variants of SAM-DAQ: one with the memory module removed to disable temporal modeling (denoted as A1), and the original SAM-DAQ with temporal modeling retained (denoted as A2). SAM-DAQ is the current best-performing SAM2-based method that also relies only on RGB and depth modalities. As shown in [Table 2](#fig7), although B1 performs worse than our full model, it still achieves SOTA performance and outperforms both A1 and A2. We further evaluate a second variant that retains optical flow while removing depth (denoted as B2), which also achieves state-of-the-art performance and outperforms A2. These findings not only confirm the effectiveness of our core architectural design but also support the inclusion of optical flow for stronger spatiotemporal modeling.

We then evaluate the effectiveness of the two core modules in our model, CP adapter and parallel LoRA. To this end, we conduct ablation experiments by removing each module individually. Specifically, C1 denotes the variant with both modules removed, C2 denotes the variant with only the parallel LoRA removed, and C3 denotes the variant with only the CP adapter removed. The results show that removing either module leads to performance degradation compared with the full model. Compared with the baseline that retains only SAM2 (with both modules removed), adding the parallel LoRA brings a substantial performance gain, whereas adding the CP adapter alone yields only a limited improvement. This may be because the three parallel LoRA modules help the model better capture the differences among the three modalities, thereby adapting the pre-trained SAM2, which was not originally trained on depth or optical flow, more effectively to these additional modalities. As a result, relying solely on the CP adapter to identify and fuse shared information across modalities is insufficient. However, when the CP adapter is introduced on top of the parallel LoRA, the two modules complement each other, leading to further performance gains and the best overall performance. In addition, C4 replaces the three parallel LoRA modules with a single LoRA module. This variant also performs worse than the full model, further confirming the effectiveness of the parallel LoRA design.

---

## References

[1] <a id="ref1"></a> D.-P. Fan, W. Wang, M.-M. Cheng, and J. Shen, “Shifting more attention to video salient object detection,” in <em>Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)</em>, 2019, pp. 8554–8564.

[2] <a id="ref2"></a> W. Wang, J. Shen, J. Xie, M.-M. Cheng, H. Ling, and A. Borji, “Revisiting video saliency prediction in the deep learning era,” <em>IEEE Transactions on Pattern Analysis and Machine Intelligence</em>, vol. 43, no. 1, pp. 220–237, 2019.

[3] <a id="ref3"></a> A. Mou, Y. Lu, J. He, D. Min, K. Fu, and Q. Zhao, “Salient object detection in RGB-D videos,” <em>IEEE Transactions on Image Processing</em>, vol. 33, pp. 6660–6675, 2024.

[4] <a id="ref4"></a> D.-P. Fan, Z. Lin, Z. Zhang, M. Zhu, and M.-M. Cheng, “Rethinking RGB-D salient object detection: Models, data sets, and large-scale benchmarks,” <em>IEEE Transactions on Neural Networks and Learning Systems</em>, vol. 32, no. 5, pp. 2075–2089, 2020.

[5] <a id="ref5"></a> H. Peng, B. Li, W. Xiong, W. Hu, and R. Ji, “RGBD salient object detection: A benchmark and algorithms,” in <em>European Conference on Computer Vision (ECCV)</em>, 2014, pp. 92–109.

[6] <a id="ref6"></a> N. Liu, N. Zhang, L. Shao, and J. Han, “Learning selective mutual attention and contrast for RGB-D saliency detection,” <em>IEEE Transactions on Pattern Analysis and Machine Intelligence</em>, vol. 44, no. 12, pp. 9026–9042, 2021.

[7] <a id="ref7"></a> F. Perazzi, J. Pont-Tuset, B. McWilliams, L. Van Gool, M. Gross, and A. Sorkine-Hornung, “A benchmark dataset and evaluation methodology for video object segmentation,” in <em>Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)</em>, 2016, pp. 724–732.

[8] <a id="ref8"></a> J. Li, W. Ji, S. Wang, W. Li, et al., “DVSOD: RGB-D video salient object detection,” in <em>Advances in Neural Information Processing Systems (NeurIPS)</em>, vol. 36, pp. 8774–8787, 2023.

[9] <a id="ref9"></a> J. Lin, L. Zhu, J. Shen, H. Fu, Q. Zhang, and L. Wang, “VidSOD-100: A new dataset and a baseline model for RGB-D video salient object detection,” <em>International Journal of Computer Vision</em>, vol. 132, no. 11, pp. 5173–5191, 2024.

[10] <a id="ref10"></a> Y. Lu, D. Min, K. Fu, and Q. Zhao, “Depth-cooperated trimodal network for video salient object detection,” in <em>2022 IEEE International Conference on Image Processing (ICIP)</em>, pp. 116–120, 2022.

[11] <a id="ref11"></a> J. Lin, X. Zhou, J. Liu, R. Cong, G. Zhang, Z. Liu, and J. Zhang, “SAM-DAQ: Segment Anything Model with Depth-guided Adaptive Queries for RGB-D Video Salient Object Detection,” in <em>Proceedings of the 40th AAAI Conference on Artificial Intelligence (AAAI)</em>, Singapore, Jan. 2026. (accepted)

[12] <a id="ref12"></a> N. Ravi, V. Gabeur, Y.-T. Hu, R. Hu, C. Ryali, T. Ma, H. Khedr, R. Rädie, C. Rolland, L. Gustafson, et al., “SAM 2: Segment anything in images and videos,” <em>arXiv preprint arXiv:2408.00714</em>, 2024.
