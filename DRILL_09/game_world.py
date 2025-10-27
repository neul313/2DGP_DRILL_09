# game 내의 객체들의 생성과 소멸을 관리하는 모듈입니다.

# 게임 내 객체들을 담는 리스트
# world[0] : 0 layer
# world[1] : 1 layer

world = [[],[]]

# 게임 내 객체를 추가하는 함수
def add_object(o, depth =0):
    world[depth].append(o)

#게임 월드에 객체 리스틑를 추가하는 함수
def add_objects(ol, depth =0): #add_objects([ball1, ball2])
    world[depth] += ol

# 게임 월드의 모든 객체들을 업데이트
def update():
    for layer in world:
        for o in layer:
            o.update()


# 게임 월드의 모든 객체들을 그리기
def render():
    for layer in world:
        for o in layer:
            o.draw()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

    raise Exception("월드에 존재하지 않은 객체를 삭제하려고 합니다.")


