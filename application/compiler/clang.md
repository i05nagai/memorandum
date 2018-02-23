# clang

## debug


### no template named '' in namespace 'std'
無名名前空間への就職

```
In file included from /home/travis/build/i05nagai/algorithms/submodule/googletest/googlemock/src/gmock-all.cc:40:
In file included from /home/travis/build/i05nagai/algorithms/submodule/googletest/googlemock/include/gmock/gmock.h:58:
/home/travis/build/i05nagai/algorithms/submodule/googletest/googlemock/include/gmock/gmock-actions.h:102:19: error: 
      no template named 'is_default_constructible' in namespace 'std'; did you
      mean 'is_nothrow_constructible'?
    return ::std::is_default_constructible<T>::value;
           ~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~
                  is_nothrow_constructible
```


