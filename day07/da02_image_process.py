from tkinter import *
from PIL import Image, ImageTk

# 퀵 정렬 구현
def sortQuickN(ary, start, end):
    global count
    if end <= start: 
        return  # 재귀호출 종료 조건

    low, high = start, end    
    pivot = ary[(low + high) // 2]  # 중간값을 기준으로 설정

    while low <= high:
        while ary[low] < pivot:
            low += 1
        while ary[high] > pivot:
            high -= 1
        if low <= high:
            ary[low], ary[high] = ary[high], ary[low]
            low, high = low + 1, high - 1
            count += 1

    mid = low
    sortQuickN(ary, start, mid - 1)  # 왼쪽 그룹 정렬
    sortQuickN(ary, mid, end)        # 오른쪽 그룹 정렬

# 변수 초기화
count = 0

# Tkinter 창 설정
root = Tk()
root.geometry('600x600')
root.title('이미지 처리(퀵 정렬)')

# 이미지 로드 (PIL 사용)
image_path = "./image/cupdog.png"
image = Image.open(image_path).convert("RGB")  # RGB 변환
w, h = image.size  # 이미지 크기 가져오기
photo = ImageTk.PhotoImage(image)

# 픽셀 데이터 가져오기
photoAry = []
for y in range(h):
    for x in range(w):
        r, g, b = image.getpixel((x, y))
        value = (r + g + b) // 3  # 평균값(그레이스케일)
        photoAry.append(value)

# 퀵 정렬 실행
dataAry = photoAry[:]
sortQuickN(dataAry, 0, len(dataAry) - 1)
midValue = dataAry[len(dataAry) // 2]  # 중간값 찾기

# 이진화 처리 (Thresholding)
for i in range(len(photoAry)):
    photoAry[i] = 0 if photoAry[i] <= midValue else 255

# 새로운 이미지 생성
new_image = Image.new("L", (w, h))  # 'L' 모드는 흑백
new_image.putdata(photoAry)  # 정렬된 픽셀 데이터 적용
new_photo = ImageTk.PhotoImage(new_image)

# Tkinter UI 적용
paper = Label(root, image=new_photo)
paper.pack(expand=1, anchor=CENTER)

root.mainloop()
