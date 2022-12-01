class CollisionChecker:
    '''Class that checks the collisions in the game'''
    
    @classmethod # This is a class method meaning that it can be called without creating an instance of the class
    def checkCollision(cls, ob1, ob2):
        '''Checks if the ob1(object1) and ob2(object2) are overlapping'''
        if ob1.x < ob2.x + ob2.width and ob1.x + ob1.width > ob2.x and ob1.y < ob2.y + ob2.height and ob1.height + ob1.y > ob2.y:
            return True
        else:
            return False
    
    # TODO: Remove this code
    # def checkCollisionList(ob1: object, ob2List: list):
    #     ''' Checks if the ob1(object1) and any object in ob2List(object2List) are overlapping'''
    #     for ob2 in ob2List:  
    #         if CollisionChecker.checkCollision(ob1, ob2):
    #             return True
    #     return False
    
    # def checkCollisionListList(ob1List: list, ob2List: list):
    #     ''' Checks if any object in ob1List(object1List) and any object in ob2List(object2List) are overlapping'''
    #     for ob1 in ob1List:
    #         for ob2 in ob2List:
    #             if CollisionChecker.checkCollision(ob1, ob2):
    #                 return True
    #     return False