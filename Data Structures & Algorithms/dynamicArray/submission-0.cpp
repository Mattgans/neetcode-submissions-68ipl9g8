
class DynamicArray {
public:
    int size = 0;
    int cap = 0;
    int* vec;

    DynamicArray(int capacity) {
        size = 0;
        cap = capacity;
        vec = new int[cap];
    }

    int get(int i) {
        return vec[i];
    }

    void set(int i, int n) {
        vec[i] = n;
    }

    void pushback(int n) {
        if (size == cap){
            resize();
        }
        vec[size] = n;
        size++;
        
    }

    int popback() {
        if (size > 0){
            size--;
        }
        return vec[size];

    }

    void resize() {
        cap *= 2;
        int* newArr = new int[cap];
        for (int i = 0; i < size; i++){
            newArr[i] = vec[i];
        }
        delete[] vec;
        vec = newArr;

    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return cap;
    }
};
