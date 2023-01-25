---
title: react typescript
---

## react typescript



## Context
https://stackoverflow.com/questions/53575461/react-typescript-context-in-react-component-class

```
export class Game extends React.Component<object, GameState> {
    static contextType = Context.AppContext;
    declare context: React.ContextType<typeof Context.AppContext>;

    constructor(props: object) {
        super(props);
    }
    public render() {
        return (
            <div>{this.context.theme}</div>
        );
    }
}
```

## Reference
- https://react-typescript-cheatsheet.netlify.app/docs/basic/setup
