import hashlib
from pickle_hash import hash_code_hex,serialize
from server_config import NODES

class NodeRing():

    def __init__(self, nodes):
        assert len(nodes) > 0
        self.nodes = nodes
        self.virtualnodes = 32
        self.vnode_to_node = []
        for vnode_id in range(self.virtualnodes):
            self.vnode_to_node.append(vnode_id % len(self.nodes))            
    
    def get_node(self, key_hex):
        key = int(key_hex, 16)
        vnode_index = key % self.virtualnodes
        node_index = self.vnode_to_node[vnode_index]
        return self.nodes[node_index]  
    
    def get_replication_node(self, key_hex):
        key = int(key_hex, 16)
        vnode_index = key % self.virtualnodes
        node_index = self.vnode_to_node[vnode_index]
        node_index+=1
        node_index%=len(self.nodes)
        return self.nodes[node_index]

def test():
    ring = NodeRing(nodes=NODES)
    node = ring.get_node('9ad5794ec94345c4873c4e591788743a')
    print(node)
    print(ring.get_node('ed9440c442632621b608521b3f2650b8'))

if __name__ == "__main__":
    test()
