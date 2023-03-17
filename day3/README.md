controlling both the limb joints with seperate sliders for upper and lower joints

![buggycode1](https://user-images.githubusercontent.com/91419527/226056024-b306a66d-956d-49ab-b28c-c03d8d6000f2.gif)

### THIS CODE HAS A BUG
if the sliders are operated in this order: knee -> hip -> knee
then the new knee angle will simply be added to the previous knee angle instead of being recalculated and readjusted

![buggycode2](https://user-images.githubusercontent.com/91419527/226056696-1c15ee36-b0f2-495e-a0d2-26bc8ca9f7fd.gif)
