class MyHashMap
{
private:
    vector<int> mymap = vector<int>(10000000, -1);

public:
    MyHashMap()
    {
    }

    void put(int key, int value)
    {
        mymap[key] = value;
    }

    int get(int key)
    {
        return mymap[key];
    }

    void remove(int key)
    {
        mymap[key] = -1;
    }
};


/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */