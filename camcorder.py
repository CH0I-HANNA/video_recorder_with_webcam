import cv2 as cv
import datetime

def run_video_recorder():
    # [필수] cv.VideoCapture를 이용하여 카메라 영상 얻기 
    cap = cv.VideoCapture(0)
    
    if not cap.isOpened():
        print("카메라를 열 수 없습니다.")
        return

    # 카메라 설정값(해상도) 가져오기
    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    fps = 30.0 
    
    # [필수] cv.VideoWriter를 이용하여 동영상 파일 만들기 
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = None
    
    # 상태 관리 변수
    is_recording = False # [필수] Preview와 Record 모드 도입 
    filter_mode = 1 # 1: 일반, 2: 그레이, 3: 캐니, 4: 좌우반전

    while cap.isOpened():
        ret, frame = cap.read() # [필수] 화면에 현재 카메라 영상 표시 
        if not ret:
            break

        # [추가 기능] 실시간 필터 전환 (각자 원하는 추가 기능)
        if filter_mode == 2:
            frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            frame = cv.cvtColor(frame, cv.COLOR_GRAY2BGR) 
        elif filter_mode == 3:
            frame = cv.Canny(frame, 100, 200)
            frame = cv.cvtColor(frame, cv.COLOR_GRAY2BGR) 
        elif filter_mode == 4:
            frame = cv.flip(frame, 1)

        # [추가 기능] 타임스탬프 삽입 (CCTV 스타일)
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cv.putText(frame, now, (10, height - 20), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv.LINE_AA)

        # [추가 기능] 중앙 상단 조작 가이드 (글씨 크기 확대 및 주황색)
        guide_text = "Space: REC/STOP | 1-4: Filter | ESC: Exit"
        font = cv.FONT_HERSHEY_SIMPLEX
        font_scale = 0.8  # 글씨 크기 키움
        thickness = 2
        orange_color = (0, 165, 255) # 주황색 (BGR)

        # 가로 중앙 계산
        text_size, _ = cv.getTextSize(guide_text, font, font_scale, thickness)
        text_x = (width - text_size[0]) // 2
        text_y = 50 # 중앙 상단 위치 (상단에서 50픽셀 아래)
        cv.putText(frame, guide_text, (text_x, text_y), font, font_scale, orange_color, thickness, cv.LINE_AA)

        # [필수] Record 모드 시 화면에 표시 
        if is_recording:
            # 녹화 표시 (가이드와 겹치지 않게 좌측 상단 배치)
            cv.circle(frame, (30, 80), 10, (0, 0, 255), -1)
            cv.putText(frame, "REC", (50, 90), font, 0.7, (0, 0, 255), 2)
            
            # [필수] 카메라 영상을 동영상 파일로 저장 
            if out is not None:
                out.write(frame)

        # 최종 화면 표시
        cv.imshow('Video Recorder', frame)

        key = cv.waitKey(1) & 0xFF
        
        # [필수] ESC 키에 프로그램 종료 
        if key == 27:
            break
            
        # [필수] Space 키에 모드 변환 
        elif key == ord(' '):
            is_recording = not is_recording
            if is_recording:
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                out = cv.VideoWriter(f'record_{timestamp}.avi', fourcc, fps, (width, height))
            else:
                if out:
                    out.release()
                    out = None
                
        # [추가 기능] 숫자 키로 필터 변경
        elif ord('1') <= key <= ord('4'):
            filter_mode = int(chr(key))

    cap.release()
    if out:
        out.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    run_video_recorder()