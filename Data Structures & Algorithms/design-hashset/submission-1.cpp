class MyHashSet {
private: 
vector<bool> myhash = vector<bool>(100000,false);
public:
    MyHashSet() {
    }
    
    void add(int key) {
        myhash[key] = true;
    }
    
    void remove(int key) {
        myhash[key] = false;
    }
    
    bool contains(int key) {
        return myhash[key];
    }
};