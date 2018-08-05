#!/usr/bin/env python
#-*- coding: utf-8 -*-


# 파일 사용은
# open('파일이름', '모드')
# 
# 모드
# r:    텍스트 모드로 읽기
# w:    텍스트 모드로 쓰기
# a:    텍스트 모드로 파일 마지막에 추가
# rb:   바이너리 모드로 읽기
# wb:   바이너리 모드로 쓰기
# ab:   바이너리 모드로 파일 마지막에 추가하기

f1 = open('047_module_import_as.py', 'r')

# 윈도우 사용자는 파일의 총경로를 입력한다. 
f2 = open('/home/ryan/Downloads/hanjimin.jpg', 'rb')

#
# 오픈한 파일을 처리하는 코드를 작성
#

# 항상 파일을 열었으면 아래 닫는 코드를 필수로 해야 함. 
# 닫지 않으면 메모리 누수 현상 발생하여 코드가 제대로 실행되지 않거나, 코드는 실행되나 다른 코드에 영향을  줄 수 있음

f1.close()
f2.close()