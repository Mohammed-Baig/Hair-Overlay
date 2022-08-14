from cv2 import cv2
import cvzone
import random


def two_load(destination1, x1_multiplier, y1_multiplier, x1_location, y1_location, destination2, x2_multiplier,
             y2_multiplier, x2_location, y2_location):
    cap = cv2.VideoCapture(0)
    cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    overlay1 = cv2.imread(destination1, cv2.IMREAD_UNCHANGED)
    overlay2 = cv2.imread(destination2, cv2.IMREAD_UNCHANGED)
    while True:
        _, frame = cap.read()
        gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray_scale)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            overlay1_resize = cv2.resize(overlay1, (int(w * x1_multiplier), int(h * y1_multiplier)))
            frame = cvzone.overlayPNG(frame, overlay1_resize, [x - x1_location, y - y1_location])

            overlay2_resize = cv2.resize(overlay2, (int(w * x2_multiplier), int(h * y2_multiplier)))
            frame = cvzone.overlayPNG(frame, overlay2_resize, [x - x2_location, y - y2_location])

        cv2.imshow('Snap Dude', frame)
        if cv2.waitKey(10) == ord('q'):
            break

    cv2.destroyAllWindows()


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
          "hair\n3.top hat\n4.custom hair \n5.random hair\n6.go back")

    x = int(input("Enter what you would like to try on here:"))
    if (x == 1):
        load('hair/basic hair.png', 3, 2, 175, 160)
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
        file_path = str(input("Enter file path here:"))
        name = '{}'.format(file_path)
        load(name, 1.5, 1.5, 45, 75)
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

    elif (x == 5):
        z = random.randint(1, 3)
        if (z == 1):
            load('hair/basic hair.png', 3, 2, 175, 160)
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

        elif (z == 2):
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

        elif (z == 3):
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

        else:
            print("invalid input, please try again later")
            quit()

    elif (x == 6):
        main()

    else:
        print("invalid input, please try again")
        quit()


def glasses():
    print("you have chosen glasses. Please choose what glasses you would like to try first\n1.plain "
          "sunglasses\n2.rhinestone glasses\n3.star sunglasses\n4.red sunglasses\n5.custom sunglasses\n6.random "
          "sunglasses\n7.go back")
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
        file_path = str(input("Enter file path here:"))
        name = '{}'.format(file_path)
        load(name, 1.5, 1.5, 45, 75)
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

    elif (x == 6):
        z = random.randint(1, 4)
        if (z == 1):
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

        elif (z == 2):
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

        elif (z == 3):
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

        elif (z == 4):
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


        else:
            print("invalid input, please try again later")
            quit()

    elif (x == 7):
        main()

    else:
        print("invalid input, please try again")
        quit()


def facial_hair():
    print("you have chosen facial hair. Please choose what facial hair you would like to try first\n1.full "
          "beard\n2.hipster beard\n3.mustache and goatee combo\n4.mustache\n5.custom facial hair\n6.random\n7.go "
          "back\nNOTE: for detection, it helps to keep the camera at a bit of a distance between your face and it")
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

    elif (x == 5):
        file_path = str(input("Enter file path here:"))
        name = '{}'.format(file_path)
        load(name, 1.5, 1.5, 45, -75)
        y = int(input("would you like to\n1.try other facial hairstyles\n2.go to main menu\n3.close app\n"))
        if (y == 1):
            facial_hair()

        elif (y == 2):
            main()

        elif (y == 3):
            quit()

        else:
            print("invalid, please try again later")
            quit()

    elif (x == 6):
        z = random.randint(1, 4)
        if (z == 1):
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

        elif (z == 2):
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

        elif (z == 3):
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

        elif (z == 4):
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

        else:
            print("invalid input, please try again later")
            quit()

    elif (x == 7):
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


def mix_and_match():
    print("choose what combination of items you would like to try\n1.Hair and Beard\n2.Hair and Glasses\n3.Beard and "
          "Glasses\n4.return to main menu")

    x = int(input("Enter what you would like to try on here"))
    if (x == 1):
        y = int(input("you have chosen hair. Please choose what hairstyle you would like to try first\n1.basic "
                      "hair\n2.white hair\n3.top hat\n4.custom"))
        z = int(input("you have chosen facial hair. Please choose what facial hair you would like to try first\n1.full "
                      "beard\n2.hipster beard\n3.mustache and goatee combo\n4.custom"))
        if (y == 1):
            if (z == 1):
                two_load('hair/basic hair.png', 3, 2, 175, 160, 'beard/Full Beard.png', 2, 2.2, 65, 20)

            elif (z == 2):
                two_load('hair/basic hair.png', 3, 2, 175, 160, 'beard/hippy beard.png', 1.5, 1.5, 40, -20)

            elif (z == 3):
                two_load('hair/basic hair.png', 3, 2, 175, 160, 'beard/Mustach+goatee.png', 1.5, 1.5, 35, -30)

            elif (z == 4):
                file_path = str(input("Enter file path here:"))
                name = '{}'.format(file_path)
                two_load('hair/basic hair.png', 3, 2, 175, 160, name, 1.5, 1.5, 45, -75)

            else:
                print("invalid input, try again later")
                quit()

        elif (y == 2):
            if (z == 1):
                two_load('hair/chadcut.png', 1.3, 0.5, 20, 40, 'beard/Full Beard.png', 2, 2.2, 65, 20)

            elif (z == 2):
                two_load('hair/chadcut.png', 1.3, 0.5, 20, 40, 'beard/hippy beard.png', 1.5, 1.5, 40, -20)

            elif (z == 3):
                two_load('hair/chadcut.png', 1.3, 0.5, 20, 40, 'beard/Mustach+goatee.png', 1.5, 1.5, 35, -30)

            elif (z == 4):
                file_path = str(input("Enter file path here:"))
                name = '{}'.format(file_path)
                two_load('hair/chadcut.png', 1.3, 0.5, 20, 40, name, 1.5, 1.5, 45, -75)

            else:
                print("invalid input, please try again later")
                quit()

        elif (y == 3):
            if (z == 1):
                two_load('hair/top hat.png', 1.5, 1, 40, 150, 'beard/Full Beard.png', 2, 2.2, 65, 20)

            elif (z == 2):
                two_load('hair/top hat.png', 1.5, 1, 40, 150, 'beard/hippy beard.png', 1.5, 1.5, 40, -20)

            elif (z == 3):
                two_load('hair/top hat.png', 1.5, 1, 40, 150, 'beard/Mustach+goatee.png', 1.5, 1.5, 35, -30)

            elif (z == 4):
                file_path = str(input("Enter file path here:"))
                name = '{}'.format(file_path)
                two_load('hair/top hat.png', 1.5, 1, 40, 150, name, 1.5, 1.5, 45, -75)

            else:
                print("invalid input, please try again later")
                quit()

        elif (y == 4):
            file_path = str(input("Enter file path here:"))
            name = '{}'.format(file_path)
            if (z == 1):
                two_load(name, 1.5, 1.5, 45, 75, 'beard/Full Beard.png', 2, 2.2, 65, 20)

            elif (z == 2):
                two_load(name, 1.5, 1.5, 45, 75, 'beard/hippy beard.png', 1.5, 1.5, 40, -20)

            elif (z == 3):
                two_load(name, 1.5, 1.5, 45, 75, 'beard/Mustach+goatee.png', 1.5, 1.5, 35, -30)

            elif (z == 4):
                file_path = str(input("Enter file path here:"))
                name2 = '{}'.format(file_path)
                two_load(name, 1.5, 1.5, 45, 75, name2, 1.5, 1.5, 45, -75)

            else:
                print("invalid input, please try again later")
                quit()

        else:
            print("Invalid input, please try again later")
            quit()

    elif (x == 2):
        y = int(input("you have chosen hair. Please choose what hairstyle you would like to try first\n1.basic "
                      "hair\n2.white hair\n3.top hat\n4.custom"))
        z = int(input("you have chosen glasses. Please choose what glasses you would like to try first\n1.plain "
                      "sunglasses\n2.rhinestone glasses\n3.star sunglasses\n4.red sunglasses\n5.custom"))
        if (y == 1):
            if (z == 1):
                two_load('hair/basic hair.png', 3, 2, 175, 160, 'glasses/plain sunglasses.png', 2, 1, 70, 10)

            elif (z == 2):
                two_load('hair/basic hair.png', 3, 2, 175, 160, 'glasses/rhinestone glasses.png', 1, 0.5, 0, -15)

            elif (z == 3):
                two_load('hair/basic hair.png', 3, 2, 175, 160, 'glasses/star.png', 1, 1, 0, 15)

            elif (z == 4):
                two_load('hair/basic hair.png', 3, 2, 175, 160, 'glasses/sunglass.png', 1, 1, 0, 15)

            elif (z == 5):
                file_path = str(input("Enter file path here:"))
                name = '{}'.format(file_path)
                two_load('hair/basic hair.png', 3, 2, 175, 160, name, 1.5, 1.5, 45, 75)

            else:
                print("invalid input, try again later")
                quit()

        elif (y == 2):
            if (z == 1):
                two_load('hair/chadcut.png', 1.3, 0.5, 20, 40, 'glasses/plain sunglasses.png', 2, 1, 70, 10)

            elif (z == 2):
                two_load('hair/chadcut.png', 1.3, 0.5, 20, 40, 'glasses/rhinestone glasses.png', 1, 0.5, 0, -15)

            elif (z == 3):
                two_load('hair/chadcut.png', 1.3, 0.5, 20, 40, 'glasses/star.png', 1, 1, 0, 15)

            elif (z == 4):
                two_load('hair/chadcut.png', 1.3, 0.5, 20, 40, 'glasses/sunglass.png', 1, 1, 0, 15)

            elif (z == 5):
                file_path = str(input("Enter file path here:"))
                name = '{}'.format(file_path)
                two_load('hair/chadcut.png', 1.3, 0.5, 20, 40, name, 1.5, 1.5, 45, 75)

            else:
                print("invalid input, please try again later")
                quit()

        elif (y == 3):
            if (z == 1):
                two_load('hair/top hat.png', 1.5, 1, 40, 150, 'glasses/plain sunglasses.png', 2, 1, 70, 10)

            elif (z == 2):
                two_load('hair/top hat.png', 1.5, 1, 40, 150, 'glasses/rhinestone glasses.png', 1, 0.5, 0, -15)

            elif (z == 3):
                two_load('hair/top hat.png', 1.5, 1, 40, 150, 'glasses/star.png', 1, 1, 0, 15)

            elif (z == 4):
                two_load('hair/top hat.png', 1.5, 1, 40, 150, 'glasses/sunglass.png', 1, 1, 0, 15)

            elif (z == 5):
                file_path = str(input("Enter file path here:"))
                name = '{}'.format(file_path)
                two_load('hair/top hat.png', 1.5, 1, 40, 150, name, 1.5, 1.5, 45, 75)

            else:
                print("invalid input, please try again later")
                quit()

        elif (y == 4):
            file_path = str(input("Enter file path here:"))
            name = '{}'.format(file_path)
            if (z == 1):
                two_load(name, 1.5, 1.5, 45, 75, 'glasses/plain sunglasses.png', 2, 1, 70, 10)

            elif (z == 2):
                two_load(name, 1.5, 1.5, 45, 75, 'glasses/rhinestone glasses.png', 1, 0.5, 0, -15)

            elif (z == 3):
                two_load(name, 1.5, 1.5, 45, 75, 'glasses/star.png', 1, 1, 0, 15)

            elif (z == 4):
                two_load(name, 1.5, 1.5, 45, 75, 'glasses/sunglass.png', 1, 1, 0, 15)

            elif (z == 5):
                file_path = str(input("Enter file path here:"))
                name2 = '{}'.format(file_path)
                two_load(name, 1.5, 1.5, 45, 75, name2, 1.5, 1.5, 45, 75)

            else:
                print("invalid input, please try again later")
                quit()

        else:
            print("Invalid input, please try again later")
            quit()

    elif (x == 3):
        y = int(input("you have chosen facial hair. Please choose what facial hair you would like to try first\n1.full "
                      "beard\n2.hipster beard\n3.mustache and goatee combo\n4.custom"))

        z = int(input("you have chosen glasses. Please choose what glasses you would like to try first\n1.plain "
                      "sunglasses\n2.rhinestone glasses\n3.star sunglasses\n4.red sunglasses\n5.custom"))
        if (y == 1):
            if (z == 1):
                two_load('beard/Full Beard.png', 2, 2.2, 65, 20, 'glasses/plain sunglasses.png', 2, 1, 70, 10)

            elif (z == 2):
                two_load('beard/Full Beard.png', 2, 2.2, 65, 20, 'glasses/rhinestone glasses.png', 1, 0.5, 0, -15)

            elif (z == 3):
                two_load('beard/Full Beard.png', 2, 2.2, 65, 20, 'glasses/star.png', 1, 1, 0, 15)

            elif (z == 4):
                two_load('beard/Full Beard.png', 2, 2.2, 65, 20, 'glasses/sunglass.png', 1, 1, 0, 15)

            elif (z == 5):
                file_path = str(input("Enter file path here:"))
                name = '{}'.format(file_path)
                two_load('beard/Full Beard.png', 2, 2.2, 65, 20, name, 1.5, 1.5, 45, 75)

            else:
                print("invalid input, try again later")
                quit()

        elif (y == 2):
            if (z == 1):
                two_load('beard/hippy beard.png', 1.5, 1.5, 40, -20, 'glasses/plain sunglasses.png', 2, 1, 70, 10)

            elif (z == 2):
                two_load('beard/hippy beard.png', 1.5, 1.5, 40, -20, 'glasses/rhinestone glasses.png', 1, 0.5, 0, -15)

            elif (z == 3):
                two_load('beard/hippy beard.png', 1.5, 1.5, 40, -20, 'glasses/star.png', 1, 1, 0, 15)

            elif (z == 4):
                two_load('beard/hippy beard.png', 1.5, 1.5, 40, -20, 'glasses/sunglass.png', 1, 1, 0, 15)

            elif (z == 5):
                file_path = str(input("Enter file path here:"))
                name = '{}'.format(file_path)
                two_load('beard/hippy beard.png', 1.5, 1.5, 40, -20, name, 1.5, 1.5, 45, 75)

            else:
                print("invalid input, please try again later")
                quit()

        elif (y == 3):
            if (z == 1):
                two_load('beard/Mustach+goatee.png', 1.5, 1.5, 35, -30, 'glasses/plain sunglasses.png', 2, 1, 70, 10)

            elif (z == 2):
                two_load('beard/Mustach+goatee.png', 1.5, 1.5, 35, -30, 'glasses/rhinestone glasses.png', 1, 0.5, 0, -15)

            elif (z == 3):
                two_load('beard/Mustach+goatee.png', 1.5, 1.5, 35, -30, 'glasses/star.png', 1, 1, 0, 15)

            elif (z == 4):
                two_load('beard/Mustach+goatee.png', 1.5, 1.5, 35, -30, 'glasses/sunglass.png', 1, 1, 0, 15)

            elif (z == 5):
                file_path = str(input("Enter file path here:"))
                name = '{}'.format(file_path)
                two_load('beard/Mustach+goatee.png', 1.5, 1.5, 35, -30, name, 1.5, 1.5, 45, 75)

            else:
                print("invalid input, please try again later")
                quit()

        elif (y == 4):
            file_path = str(input("Enter file path here:"))
            name = '{}'.format(file_path)
            if (z == 1):
                two_load(name, 1.5, 1.5, 45, -75, 'glasses/plain sunglasses.png', 2, 1, 70, 10)

            elif (z == 2):
                two_load(name, 1.5, 1.5, 45, -75, 'glasses/rhinestone glasses.png', 1, 0.5, 0, -15)

            elif (z == 3):
                two_load(name, 1.5, 1.5, 45, -75, 'glasses/star.png', 1, 1, 0, 15)

            elif (z == 4):
                two_load(name, 1.5, 1.5, 45, -75, 'glasses/sunglass.png', 1, 1, 0, 15)

            elif (z == 5):
                file_path = str(input("Enter file path here:"))
                name2 = '{}'.format(file_path)
                two_load(name, 1.5, 1.5, 45, -75, name2, 1.5, 1.5, 45, 75)

            else:
                print("invalid input, please try again later")
                quit()

        else:
            print("Invalid input, please try again later")
            quit()

    elif (x == 4):
        main()

    else:
        print("invalid input, please try again later")
        quit()


def main():
    print("What would you like to try on?")
    print("1.Hair\n2.Glasses\n3.Facial Hair\n4.Full Ensemble\n5.mix and match\n6.close program")
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
        mix_and_match()

    elif (x == 6):
        quit()

    else:
        print("invalid input")


if __name__ == "__main__":
    main()
