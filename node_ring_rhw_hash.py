import hashlib
from pickle_hash import hash_code_hex,serialize
from server_config import NODES

class NodeRing():

    def __init__(self, nodes):
        assert len(nodes) > 0
        self.nodes = nodes
    
    def get_node(self, key_hex):
        hashVal=0
        node_index=0
        for i in range(len(self.nodes)):
            obj ={}
            obj['host']=self.nodes[i]['host']
            obj['port']=self.nodes[i]['port']    
            obj['key']=key_hex 
            nodekey=int(hash_code_hex(serialize(obj)),16)
            if nodekey>hashVal:
                hashVal=nodekey
                node_index=i
        return self.nodes[node_index]

def test():
    ring = NodeRing(nodes=NODES)
    node = ring.get_node('9ad5794ec94345c4873c4e591788743a')
    print(node)
    print(ring.get_node('ed9440c442632621b608521b3f2650b8'))

if __name__ == "__main__":
    test()
