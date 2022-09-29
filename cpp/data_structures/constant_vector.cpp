// A vector with unconditional O(1) push
template <class T>
struct ConstantTimeVector {
    T* buf;
    T* next_buf;
    size_t len;
    size_t cap;

    void push(T x) {
        if (len == cap) {
            free(buf);
            buf = next_buf;
            cap *= 2;
            next_buf = alloc(cap);
        }

        buf[len] = x;
        next_buf[len] = x;
        next_buf[len - cap / 2] = buf[len - cap / 2];
        len += 1;
    }
};
