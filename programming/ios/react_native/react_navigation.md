---
title: React Navigation
---

## React Navigation


```
npm install @react-navigation/native
npm install @react-navigation/native-stack
```


## tab navigation
https://reactnavigation.org/docs/tab-based-navigation

```typescript
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";

const BottomTab = createBottomTabNavigator();

export const BottomTabNavigator = () => (
  <BottomTab.Navigator tabBar={props => <BottomTabs {...props} />}>
    <BottomTab.Screen component={Notifications} name="Notifications" />
    <BottomTab.Screen component={Profile} name="Profile" />
    <BottomTab.Screen component={Search} name="Search" />
    <BottomTab.Screen component={Home} name="Home" />
  </BottomTab.Navigator>
);
```

## Reference
- https://reactnavigation.org/
