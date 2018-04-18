import math
from enum import Enum


class NodeStorage:

    def __init__(self):
        self.nodeList = []
        self.storageSize = 0
        self.bodyID = None

    def addNodeToStorage(self, nodeID, node, bodyID):
        if self.doContainID(nodeID) == False:
            self.nodeList.append([nodeID, node, bodyID])
            self.storageSize += 1

    def printNodeStorage(self):
        for i in range(self.storageSize):
            print(self.nodeList[i][0], self.nodeList[i][1].getInfo(), self.nodeList[i][2])

    def getSize(self):
        return self.storageSize

    def getNodeUsingID(self, nodeID):
        for i in range(self.storageSize):
            if (self.nodeList[i][0] == nodeID):
                return self.nodeList[i][1]

    def getStorageElementUsingID(self, nodeID):
        for i in range(self.storageSize):
            if (self.nodeList[i][0] == nodeID):
                return self.nodeList[i]

    def doContainID(self, nodeID):
        for i in range(self.storageSize):
            if (self.nodeList[i][0] == nodeID):
                return True
        return False


class NodeDirection(Enum):
    SW = 'SW'
    NW = 'NW'
    NE = 'NE'
    SE = 'SE'
    ROOT = 'ROOT'


class Node:

    id = 0

    def __init__(self, x0, xh, y0, yh, direction):
        self.x0 = x0
        self.x1 = xh
        self.y0 = y0
        self.y1 = yh
        self.direction = direction
        self.isEmpty = True
        self.hasChildren = False

    def isBodyInNode(self, body):
        if (body.getX() > self.x0) & (body.getX() < self.x1) & (body.getY() > self.y0) & (body.getY() < self.y1):
            return True
        else:
            return False

    def addBodyToNode(self, body, nodeStorage):
        self.isEmpty = False
        nodeStorage.getStorageElementUsingID(self.id)[2] = body.id

    def divideNode(self, nodeStorage, bodyList):
        self.hasChildren = False
        SWNode = Node(self.x0, self.x1 / 2.0, self.y0, self.y1 / 2.0, NodeDirection.SW.name)
        NWNode = Node(self.x0, self.x1 / 2.0, self.y1 / 2.0, self.y1, NodeDirection.NW.name)
        NENode = Node(self.x1 / 2.0, self.x1, self.y1 / 2.0, self.y1, NodeDirection.NE.name)
        SENode = Node(self.x1 / 2.0, self.x1, self.y0, self.y1 / 2.0, NodeDirection.SE.name)
        SWNode.id = SWNode.generateNodeID(self.id)
        NWNode.id = NWNode.generateNodeID(self.id)
        NENode.id = NENode.generateNodeID(self.id)
        SENode.id = SENode.generateNodeID(self.id)
        self.addToChildNode(nodeStorage, SWNode, NWNode, NENode, SENode, bodyList)

    def addToChildNode(self, nodeStorage, SWNode, NWNode, NENode, SENode, bodyList):
        commID = nodeStorage.getStorageElementUsingID(self.id)[2]
        commBody = bodyList[commID - 1]
        if SWNode.isBodyInNode(commBody) == True:
            SWNode.isEmpty = False
            nodeStorage.addNodeToStorage(SWNode.id, SWNode, commBody.id)
        else:
            nodeStorage.addNodeToStorage(SWNode.id, SWNode, None)
        if NWNode.isBodyInNode(commBody) == True:
            NWNode.isEmpty = False
            nodeStorage.addNodeToStorage(NWNode.id, NWNode, commBody.id)
        else:
            nodeStorage.addNodeToStorage(NWNode.id, NWNode, None)
        if NENode.isBodyInNode(commBody) == True:
            NENode.isEmpty = False
            nodeStorage.addNodeToStorage(NENode.id, NENode, commBody.id)
        else:
            nodeStorage.addNodeToStorage(NENode.id, NENode, None)
        if SENode.isBodyInNode(commBody) == True:
            SENode.isEmpty = False
            nodeStorage.addNodeToStorage(SENode.id, SENode, commBody.id)
        else:
            nodeStorage.addNodeToStorage(SENode.id, SENode, None)

    def addBodyToQuadtree(self, body, nodeStorage, bodyList):
        if self.isBodyInNode(body) == True:
            if self.isEmpty == False:
                if self.hasChildren == False:
                    self.divideNode(nodeStorage, bodyList)
                    for i in range(1, 5):
                        if self.id == 0:
                            tempNode = nodeStorage.getNodeUsingID(i)
                        else:
                            tempNode = nodeStorage.getNodeUsingID(int(str(self.id) + str(i)))
                        tempNode.addBodyToQuadtree(body, nodeStorage, bodyList)
                elif self.hasChildren == True:
                    for i in range(1, 4):
                        if self.id == 0:
                            tempNode = nodeStorage.getNodeUsingID(i)
                        else:
                            tempNode = nodeStorage.getNodeUsingID(int(str(self.id) + str(i)))
                        tempNode.addBodyToQuadtree(body, nodeStorage)
            elif self.isEmpty == True:
                self.addBodyToNode(body, nodeStorage)

    def generateNodeID(self, parentNodeID):
        if self.direction == 'ROOT':
            return parentNodeID
        elif self.direction == 'SW':
            return int(str(parentNodeID) + '1')
        elif self.direction == 'NW':
            return int(str(parentNodeID) + '2')
        elif self.direction == 'NE':
            return int(str(parentNodeID) + '3')
        elif self.direction == 'SE':
            return int(str(parentNodeID) + '4')

    def getInfo(self):
        return self.id, self.x0, self.x1, self.y0, self.y1

    def getLevel(self):
        return int(math.log(1 / (self.x1 - self.x0), 2))