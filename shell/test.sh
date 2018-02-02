#!/bin/sh

# test create file with function
createFile(){
    echo '-----START: test create file -----'
    
    cd ~
    mkdir temp
    cd temp

    for i in $(seq 10)
        do
            touch test_$i.txt
        done

    echo '-----END.-----'
}

createFile


#设置文件可执行
#chmod +x filename