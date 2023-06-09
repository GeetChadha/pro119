import cv2

def drawBox(img, bbox):
    x, y, w, h = bbox
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.putText(img, "Tracking", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

def goal_track(img, bbox):
    
    pass

def main():
   
    tracker = cv2.TrackerCSRT_create()

   
    video = cv2.VideoCapture("your_video_file.mp4")

    
    success, img = video.read()

   
    bbox = cv2.selectROI("Tracking", img, False)

    
    tracker.init(img, bbox)

    while True:
        
        success, img = video.read()

        if success:
           
            success, bbox = tracker.update(img)

            if success:
               
                drawBox(img, bbox)
                goal_track(img, bbox)
            else:
             
                cv2.putText(img, "LOST", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

           
            cv2.imshow("Tracking", img)

           
            if cv2.waitKey(1) == 27:
                break
        else:
            break

    
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
