class node{
    public:
        int val;
        node* next;
        node(int value){
            val = value;
            next = NULL;
        }
};


class LinkedList {
private:
    node* head;
    node* tail;
public:
    LinkedList() {
        head = new node(-1);
        tail = head;
    }

    int get(int index) {
        node* cur = head->next;
        int count = 0;
        while(cur != NULL){
            if(count == index){
                return cur->val;
            }
            count++;
            cur = cur->next;
            
        }
        return -1;
    }

    void insertHead(int val) {
        node* new_node = new node(val);
        new_node->next = head->next;
        head->next = new_node;
        if(head == tail){
            tail = new_node;
        }
        
    }
    
    void insertTail(int val) {
        node* new_node = new node(val);
        tail->next = new_node;
        tail = new_node;
        
    }

    bool remove(int index) {
        node* cur = head;
        int count = 0;
        while(count < index && cur != NULL){
            count++;
            cur = cur->next;
        }
        if(cur != NULL && cur->next != NULL){
            if(cur->next == tail){
                tail = cur;
            }
            node* del = cur->next;
            cur->next = cur->next->next;
            delete del;
            return true;
        }
        return false;
    }

    vector<int> getValues() {
        vector<int> res;
        node* cur = head->next;
        while(cur){
            res.push_back(cur->val);
            cur = cur->next;
        }
        return res;
    }
};
