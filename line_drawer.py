import cv2
import numpy as np
def mouse_drawing(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Left click")
        points.append((x, y))



file="1.bmp"
#cap = cv2.VideoCapture(0)

cv2.namedWindow("Frame",cv2.WINDOW_NORMAL)
cv2.setMouseCallback("Frame", mouse_drawing)
points = []
list_of_points=[]
while True:
    #_, frame = cap.read()
    frame = cv2.imread("data/"+file)

    # for center_position in points:
    #     cv2.circle(frame, center_position, 5, (0, 0, 255), -1)
    for i in range(len(points)-1):
        lineThickness = 2
        cv2.line(frame, points[i], points[i+1], (0,255,0), lineThickness)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord("r"):
        print("resetting")
        points = []
        list_of_points=[]
    elif key == ord("n"):
        print("adding to list")
        list_of_points.append(points)
        print("list_of_points",list_of_points)
        points = []
    elif key == ord("d"):
        print("draw on white image")
        width=frame.shape[1]
        height=frame.shape[0]
        img = np.zeros((height,width,1), np.uint8)
        img.fill(255)
        print("blank img created")
        lineThickness = 2
        print("len(list_of_points)",len(list_of_points))

        for j in range(len(list_of_points)):
            print("len(list_of_points[j])-1",len(list_of_points[j])-1)
            for i in range(len(list_of_points[j])-1):
                points_td=list_of_points[j]
                print("points_td",points_td)
                cv2.line(img, points_td[i], points_td[i+1], (0), lineThickness)
                print("drew line")
                points = []
        cv2.imwrite("result/"+file[0]+".png",img)    
#cap.release()
cv2.destroyAllWindows()
