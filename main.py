import pygame, os, shutil


class Game:
    def __init__(self):
        self.run = True
        self.name = "Patrón"

        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.display = Display(self)

        self.desk_items = [
            Telephone(),
            Letter(),
            PenAndPaper()
        ]
    
    def update(self, keys_pressed, mouse_pressed, mousex, mousey):

        self.display.cursor.update(mousex, mousey)

        for item in self.desk_items:
            item.update(mousex, mousey)

        self.display.update()


class Display:
    def __init__(self, game):
        self.game = game

        self.WIDTH = 900
        self.HEIGHT = 700

        # background
        filepath = "assets/img/background0.png" #background0.png
        image = pygame.image.load(filepath)
        self.background = pygame.transform.scale(image, (self.WIDTH, self.HEIGHT))

        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(self.game.name)
        pygame.mouse.set_visible(False)
        self.cursor = Cursor()
    
    def update(self):
        self.WIN.blit(self.background, pygame.Rect(0, 0, self.WIDTH, self.HEIGHT))

        for item in self.game.desk_items:
            self.WIN.blit(item.sprite, item.transform.rect)

        self.WIN.blit(self.cursor.sprite, self.cursor.transform.rect)

        pygame.display.update()


class Transform:
    def __init__(self, x=0, y=0, width=1, height=1):
        if width%2 != 0:
            raise ValueError(f"Width must be divisible by 2 ({width}/2 = {width/2})")
        if height%2 != 0:
            raise ValueError(f"Height must be divisible by 2 ({height}/2 = {height/2})")
        self.x = x
        self.y =y

        self.width = width
        self.height = height

        self.left = x - width/2
        self.top = y - height/2

        self.right = x + width/2
        self.bottom = y + height/2

        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
    
    def update(self):
        self.left = self.x - self.width/2
        self.top = self.y - self.height/2

        self.right = self.x + self.width/2
        self.bottom = self.y + self.height/2

        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)

class Cursor:
    def __init__(self):
        self.transform = Transform(0, 0, 40, 40)

        filepath = "assets/img/cursor0.png"
        image = pygame.image.load(filepath)
        self.sprite = pygame.transform.scale(image, (self.transform.width, self.transform.height))
    
    def update(self, mousex, mousey):
        self.transform.x = mousex
        self.transform.y = mousey
        self.transform.update()


class Telephone:
    def __init__(self):
        self.transform = Transform(130, 400, 90, 72)

        filepath = "assets/img/telephone0.png"
        image = pygame.image.load(filepath)
        self.sprite = pygame.transform.scale(image, (self.transform.width, self.transform.height))
    
    def update(self, mousex, mousey):
        if self.transform.left < mousex < self.transform.right and \
        self.transform.top < mousey < self.transform.bottom:
            self.transform.y = 380
        else:
            self.transform.y = 400
        self.transform.update()


class Letter:
    def __init__(self):
        self.transform = Transform(250, 400, 120, 100)

        filepath = "assets/img/letter.png"
        image = pygame.image.load(filepath)
        self.sprite = pygame.transform.scale(image, (self.transform.width, self.transform.height))
    
    def update(self, mousex, mousey):
        if self.transform.left < mousex < self.transform.right and \
        self.transform.top < mousey < self.transform.bottom:
            self.transform.y = 380
        else:
            self.transform.y = 400
        self.transform.update()


class PenAndPaper:
    def __init__(self):
        self.transform = Transform(490, 440, 300, 170)

        filepath = "assets/img/penandpaper.png"
        image = pygame.image.load(filepath)
        self.sprite = pygame.transform.scale(image, (self.transform.width, self.transform.height))
    
    def update(self, mousex, mousey):
        if self.transform.left < mousex < self.transform.right and \
        self.transform.top < mousey < self.transform.bottom:
            self.transform.y = 420
        else:
            self.transform.y = 440
        self.transform.update()


def close_save():
    for filename in os.listdir("data"):
        file_path = os.path.join("data", filename)

        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # delete file
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # delete folder
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")


def load_new_save():
    source = "saves/0"
    destination = "data"

    for item in os.listdir(source):
        src = os.path.join(source, item)
        dst = os.path.join(destination, item)

        if os.path.isdir(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            shutil.copy2(src, dst)

def make_save(slot):
    source = "data"
    destination = f"saves/{slot}"

    for item in os.listdir(source):
        src = os.path.join(source, item)
        dst = os.path.join(destination, item)

        if os.path.isdir(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            shutil.copy2(src, dst)

def main():
    close_save()
    load_new_save()

    game = Game()
    while game.run:
        game.clock.tick(game.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pass

        keys_pressed = pygame.key.get_pressed()
        mouse_pressed = pygame.mouse.get_pressed()
        mousex, mousey = pygame.mouse.get_pos()

        game.update(keys_pressed, mouse_pressed, mousex, mousey)

if __name__ == "__main__":
    main()