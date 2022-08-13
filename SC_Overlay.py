from cv2 import cv2
import cvzone


def load(destination, x_multiplier, y_multiplier, x_location, y_location):
    cap = cv2.VideoCapture(0)
    cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    overlay = cv2.imread(destination, cv2.IMREAD_UNCHANGED)
    while True:
        _, frame = cap.read()
        faces = cascade.detectMultiScale(frame)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            overlay_resize = cv2.resize(overlay, (int(w * x_multiplier), int(h * y_multiplier)))
            frame = cvzone.overlayPNG(frame, overlay_resize, [x - x_location, y - y_location])

        cv2.imshow('', frame)

        if cv2.waitKey(10) == ord('q'):
            break

    cv2.destroyAllWindows()

def load_no_resize(destination, x_location, y_location):
    cap = cv2.VideoCapture(0)
    cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    overlay = cv2.imread(destination, cv2.IMREAD_UNCHANGED)
    while True:
        _, frame = cap.read()
        gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray_scale)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            frame = cvzone.overlayPNG(frame, overlay, [x - x_location, y - y_location])

        cv2.imshow('Try on', frame)

        if cv2.waitKey(10) == ord('q'):
            break

    cv2.destroyAllWindows()

def hair():
    print("you have chosen hair. Please choose what hairstyle you would like to try first\n1.basic hair\n2.white "
          "hair\n3.top hat\n4.go back")

    x = int(input("Enter what you would like to try on here:"))
    if (x == 1):
        load('hair/basic hair.png', 3, 2, 175, 160)
        y = int(input("would you like to\n1.try other hairstyles\n2.go to main menu\n3.close app\n"))
        if (y == 1):
            hair()

        elif(y == 2):
            main()

        elif(y == 3):
            quit()

        else:
            print("invalid, please try again later")
            quit()

    elif (x == 2):
        load('hair/chadcut.png', 1.3, 0.5, 20, 40)
        y = int(input("would you like to\n1.try other hairstyles\n2.go to main menu\n3.close app\n"))
        if (y == 1):
            hair()

        elif (y == 2):
            main()

        elif (y == 3):
            quit()

        else:
            print("invalid, please try again later")
            quit()

    elif (x == 3):
        load('hair/top hat.png', 1.5, 1, 40, 150)
        y = int(input("would you like to\n1.try other hairstyles\n2.go to main menu\n3.close app\n"))
        if (y == 1):
            hair()

        elif (y == 2):
            main()

        elif (y == 3):
            quit()

        else:
            print("invalid, please try again later")
            quit()

    elif (x == 4):
        main()

    else:
        print("invalid input, please try again")
        quit()

def glasses():
    print("you have chosen glasses. Please choose what glasses you would like to try first\n1.plain "
          "sunglasses\n2.rhinestone glasses\n3.star sunglasses\n4.red sunglasses\n5.go back")
    x = int(input("Enter what you would like to try on here:"))
    if (x == 1):
        load('glasses/plain sunglasses.png', 2, 1, 70, 10)
        y = int(input("would you like to\n1.try other glasses\n2.go to main menu\n3.close app\n"))
        if (y == 1):
            glasses()

        elif (y == 2):
            main()

        elif (y == 3):
            quit()

        else:
            print("invalid, please try again later")
            quit()

    elif (x == 2):
        load('glasses/rhinestone glasses.png', 1, 0.5, 0, -15)
        y = int(input("would you like to\n1.try other glasses\n2.go to main menu\n3.close app\n"))
        if (y == 1):
            glasses()

        elif (y == 2):
            main()

        elif (y == 3):
            quit()

        else:
            print("invalid, please try again later")
            quit()

    elif (x == 3):
        load('glasses/star.png', 1, 1, 0, 15)
        y = int(input("would you like to\n1.try other glasses\n2.go to main menu\n3.close app\n"))
        if (y == 1):
            glasses()

        elif (y == 2):
            main()

        elif (y == 3):
            quit()

        else:
            print("invalid, please try again later")
            quit()

    elif (x == 4):
        load('glasses/sunglass.png', 1, 1, 0, 15)
        y = int(input("would you like to\n1.try other glasses\n2.go to main menu\n3.close app\n"))
        if (y == 1):
            glasses()

        elif (y == 2):
            main()

        elif (y == 3):
            quit()

        else:
            print("invalid, please try again later")
            quit()

    elif (x == 5):
        main()

    else:
        print("invalid input, please try again")
        quit()

def facial_hair():
    print("you have chosen facial hair. Please choose what facial hair you would like to try first\n1.full "
          "beard\n2.hipster beard\n3.mustache and goatee combo\n4.mustache\n5.go back\nNOTE: for detection, "
          "it helps to keep the "
          "camera at a bit of a distance between your face and it")
    x = int(input("Enter what you would like to try on here:"))
    if (x == 1):
        load('beard/Full Beard.png', 2, 2.2, 65, 20)
        y = int(input("would you like to\n1.try other beards\n2.go to main menu\n3.close app\n"))
        if (y == 1):
            facial_hair()

        elif (y == 2):
            main()

        elif (y == 3):
            quit()

        else:
            print("invalid, please try again later")
            quit()

    elif (x == 2):
        load('beard/hippy beard.png', 1.5, 1.5, 40, -20)
        y = int(input("would you like to\n1.try other beards\n2.go to main menu\n3.close app\n"))
        if (y == 1):
            facial_hair()

        elif (y == 2):
            main()

        elif (y == 3):
            quit()

        else:
            print("invalid, please try again later")
            quit()

    elif (x == 3):
        load('beard/Mustach+goatee.png', 1.5, 1.5, 35, -30)
        y = int(input("would you like to\n1.try other beards\n2.go to main menu\n3.close app\n"))
        if (y == 1):
            facial_hair()

        elif (y == 2):
            main()

        elif (y == 3):
            quit()

        else:
            print("invalid, please try again later")
            quit()

    elif (x == 4):
        load_no_resize('beard/mustache.png', 35, -75)
        y = int(input("would you like to\n1.try other beards\n2.go to main menu\n3.close app\n"))
        if (y == 1):
            facial_hair()

        elif (y == 2):
            main()

        elif (y == 3):
            quit()

        else:
            print("invalid, please try again later")
            quit()

    elif(x == 5):
        main()

    else:
        print("invalid input, please try again")
        quit()

def ensemble():
    print("you have chosen full ensemble. Please choose what combination you would like to try first\n1.hipster "
          "combo\n2.monopoly man\n3.pirate style 1\n4.pirate style 2\n5.go back")
    x = int(input("Enter what you would like to try on here:"))
    if (x == 1):
        load('ensemble/hippy combo.png', 1.5, 1.5, 45, 75)
        y = int(input("would you like to\n1.try other combinations\n2.go to main menu\n3.close app\n"))
        if (y == 1):
            ensemble()

        elif (y == 2):
            main()

        elif (y == 3):
            quit()

        else:
            print("invalid, please try again later")
            quit()

    elif (x == 2):
        load('ensemble/monopoly man.png', 1.2, 1.2, 20, 40)
        y = int(input("would you like to\n1.try other combinations\n2.go to main menu\n3.close app\n"))
        if (y == 1):
            ensemble()

        elif (y == 2):
            main()

        elif (y == 3):
            quit()

        else:
            print("invalid, please try again later")
            quit()

    elif (x == 3):
        load('ensemble/pirate1.png', 1.6, 1.6, 55, 80)
        y = int(input("would you like to\n1.try other combinations\n2.go to main menu\n3.close app\n"))
        if (y == 1):
            ensemble()

        elif (y == 2):
            main()

        elif (y == 3):
            quit()

        else:
            print("invalid, please try again later")
            quit()

    elif (x == 4):
        load('ensemble/pirate2.png', 1.5, 1.6, 45, 75)
        y = int(input("would you like to\n1.try other combinations\n2.go to main menu\n3.close app\n"))
        if (y == 1):
            ensemble()

        elif (y == 2):
            main()

        elif (y == 3):
            quit()

        else:
            print("invalid, please try again later")
            quit()

    elif (x == 5):
        main()

    else:
        print("invalid input, please try again")
        quit()

def custom():
    type = int(input("Is this a\n1.Hairpiece\n2.Type of eyewear\n3.Facial hair style\n4:Neither and you want to go "
                     "back: "))

    if(type == 1):
        file_path = str(input("Enter file path here:"))
        name = '{}'.format(file_path)
        load(name, 1.5, 1.5, 45, 75)
        y = int(input("would you like to\n1.try other combinations\n2.go to main menu\n3.close app\n"))
        if (y == 1):
            custom()

        elif (y == 2):
            main()

        elif (y == 3):
            quit()

        else:
            print("invalid, please try again later")
            quit()

    elif (type == 2):
        file_path = str(input("Enter file path here:"))
        name = '{}'.format(file_path)
        load(name, 1.5, 1.5, 45, 75)
        y = int(input("would you like to\n1.try other combinations\n2.go to main menu\n3.close app\n"))
        if (y == 1):
            custom()

        elif (y == 2):
            main()

        elif (y == 3):
            quit()

        else:
            print("invalid, please try again later")
            quit()

    elif (type == 3):
        file_path = str(input("Enter file path here:"))
        name = '{}'.format(file_path)
        load(name, 1.5, 1.5, 45, 75)
        y = int(input("would you like to\n1.try other combinations\n2.go to main menu\n3.close app\n"))
        if (y == 1):
            custom()

        elif (y == 2):
            main()

        elif (y == 3):
            quit()

        else:
            print("invalid, please try again later")
            quit()

    elif (type == 4):
        main()

    else:
        print("invalid input, please try again")
        quit()


def mix_and_match():
    print("choose what combination of items you would like to try ")

def main():
    print("What would you like to try on?")
    print("1.Hair\n2.Glasses\n3.Facial Hair\n4.Full Ensemble\n5.Custom file\n6.mix and match\n7.close program")
    x = int(input("Enter what you would like to try on here:"))
    if (x == 1):
        hair()

    elif (x == 2):
        glasses()

    elif (x == 3):
        facial_hair()

    elif (x == 4):
        ensemble()

    elif (x == 5):
        custom()

    elif (x == 6):
        mix_and_match()

    elif (x == 7):
        quit()

    else:
        print("invalid input")

if __name__ == "__main__":
    main()