# Gombok
Alternative to Stream Deck alternatives. Changing the client (smartphone) - server architecture to just a server app and the browser on the client device.
## Name
`gombok` in Hungarian means buttons or keys.
## TODO
- [x] Initial concept implementation
  - [x] Discord toggle mute (custom keybind to test unused modifiers)
  - [x] take screenshot (open screenshot select)
- [ ] Button theming
  - [ ] CSS
  - [ ] button images
- [ ] Button feedback
  - [ ] server: return something based on the action
  - [ ] client: change button appearance based on response
- [ ] Modular button creation
  - [ ] generate buttons from some form of config file (note to self: serverside job!!!)
  - [ ] create GUI for editing config (maybe?)
- [ ] Security
  - [ ] test if only accessible from LAN
  - [ ] if not, look into options
    - [ ] server secret entered in client?