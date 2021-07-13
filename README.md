# AlgorithmTest

//별 출력( 재귀 사용)   
//---------------------------------//   
#include <stdio.h>   
   
void draw(int h);   
   
int main(void){   
    int height = get_int("input");   
   
    draw(height);   
}   
   
void draw(int h){   
    if(h==0){   
        return ;   
    }   
   
    draw(h-1);   
   
    for(int i=0;i<h;i++){   
        printf("*");   
    }   
    printf("\n");   
}   
//---------------------------------//   

파이썬 문법 확인

프로그래머스 계정하나 추가후 문제 


백준-문제-단계별로 풀어보기
정리한거 한번 복기
