import os
import cv2

# Classe responśavel pelo cadastro do usuário que será reconhecido pela câmera.

class Cadastro:
    def __init__ (self):
        self.dir = dir
        self.nome = input('Please, enter your name for registration: ')

    def criar_pasta(self):                  # Criação da pasta de cadastro.
        if not os.path.exists('records'):  # Confere se a pasta já existe.
            os.mkdir('records')
            print("The folder was created successfully!")
        self.dir = 'records'

    def tirar_foto(self, video_ou_webcam):  # Captura da imagem do usuário.
        nome_foto = self.nome + '.png'      # Nomeia imagem com o nome do usuário.
        self.dir += '/' + nome_foto         # Salva o diretório da captura.

        if os.path.exists(self.dir):        # Se o usuário já for cadastrado, não fará novamente. 
            print('You are already registered.')

        else:
            print('You are not registered, do it now!')

            # A captura pode ser feita por webcam (0) ou vídeo (1).

            if video_ou_webcam == 0:
                cap = cv2.VideoCapture(0)
            
            elif video_ou_webcam == 1:
                nome_video = input('Nome do arquivo de vídeo: ')
                cap = cv2.VideoCapture(nome_video)
            
            while True:
                try:
                    check, frame = cap.read()
                    cv2.imshow("Capturando", frame)
                    key = cv2.waitKey(1)
                    print("Press the S key to take the photo.")
                    if key == ord('s'):         # Realiza a captura pressionando a tecla "S"
                        cv2.imwrite(filename=self.dir, img=frame)
                        cap.release()
                        print("Photo saved!")
                        break
                    
                    elif key == ord('q'):
                        cap.release()
                        cv2.destroyAllWindows()
                        break
                
                except(KeyboardInterrupt):
                    print("Desligando a câmera.")
                    webcam.release()
                    print("Câmera desligada.")
                    print("Programa encerrado.")
                    cv2.destroyAllWindows()
                    break