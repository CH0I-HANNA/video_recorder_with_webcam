# 🎥 video_recorder_with_webcam
> **My simple video recorder using OpenCV**

이 프로젝트는 OpenCV를 활용하여 카메라 영상을 실시간으로 확인하고, 다양한 필터 적용 및 동영상 녹화가 가능한 비디오 레코더 프로그램입니다. 

## 🚀 주요 기능 (Key Features)

* **카메라 영상 획득**: `cv.VideoCapture`를 사용하여 실시간 웹캠 영상을 화면에 표시합니다.
* **동영상 파일 저장**: `cv.VideoWriter`를 통해 녹화된 영상을 `.avi` 파일로 컴퓨터에 저장합니다.
* **모드 시스템**: **Space** 키를 통해 'Preview' 모드와 'Record' 모드를 전환합니다.
* **녹화 상태 표시**: 녹화 중(Record 모드)일 때 화면에 **빨간색 원**과 **REC** 문구를 출력합니다.
* **종료 기능**: **ESC** 키를 누르면 프로그램이 즉시 종료됩니다.
* **실시간 필터 전환**: 숫자 키(1~4)를 통해 원본, 그레이스케일, 캐니 엣지, 좌우 반전 필터를 즉시 적용할 수 있습니다.
* **사용자 친화적 UI**: 화면 중앙 상단에 주황색 글씨로 조작법 가이드를 상시 표시하여 편의성을 높였습니다.

## ⌨️ 조작 가이드 (Controls)
| Key | Action |
| :--- | :--- |
| **Space** | **녹화 시작 및 중지** (Preview ↔ Record) |
| **1** | **Original**: 필터가 없는 원본 영상 |
| **2** | **Grayscale**: 흑백 필터 적용 |
| **3** | **Canny Edge**: 외곽선 검출 필터 적용 |
| **4** | **Flip**: 좌우 반전 (거울 모드) |
| **ESC** | **프로그램 종료** |

## 📸 실행 화면 
## (Screenshot)
<img width="1988" height="1167" alt="Image" src="https://github.com/user-attachments/assets/44878076-2166-4af2-88b0-d993a2dfc300" />

## (video)

https://github.com/user-attachments/assets/00cb4508-515d-4242-a606-ffe3d034d97a

## 🛠️ 개발 및 실행 환경
* **Language**: Python 
* **Library**: OpenCV (`opencv-python`)
