#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from os import remove

target_file = 'stockcode_copy.text'
k = input('[%s] 파일을 삭제하겠습니까?(y/n)' %target_file)

if k == 'y':
    remove(target_file)
    print('[%s]를 삭제했습니다.' %target_file)