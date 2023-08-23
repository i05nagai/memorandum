---
title: React Native
---

## React Native


```
npm install react-native-cli
npm install react-native
npx react-native init <project-name>
```

## Run ios

```
npx react-native run-ios
```

## Components
https://reactnative.dev/docs/intro-react-native-components

- View
- ScrollView
- SafeAreaView
    - https://reactnative.dev/docs/getting-started
    - renders nested content and automatically applies padding to reflect the portion of the view that is not covered by navigation bars, tab bars, toolbars, and other ancestor views. 
- Text
- Image
- TextInput
- StatusBar
- StyleSheet
- FlatList

- useColorScheme

## platform

```
import {Platform, StyleSheet} from 'react-native';
Platform.OS === 'ios'
```

## PressEvent
- https://reactnative.dev/docs/pressevent

## Reference
* [Install React Native | Christian Engvall](https://www.christianengvall.se/install-react-native/)
* [React Native Tutorial: Building iOS Apps with JavaScript](https://www.raywenderlich.com/165140/react-native-tutorial-building-ios-android-apps-javascript)
