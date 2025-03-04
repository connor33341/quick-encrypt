#include <dlfcn.h>
#include <stdio.h>

int main(){
    void* handle = dlopen("./main.cpython-312-x86_64-linux-gnu.so",RTLD_LAZY);
    if (!handle){
        fprintf(stderr,"Error: %s\n",dlerror());
        return 1;
    }
    dlclose(handle);
    return 0;
}