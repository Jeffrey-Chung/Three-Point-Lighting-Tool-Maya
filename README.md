# Three-Point-Lighting-Tool-Maya
 Creates a Three Point Lighting System on a Selected Object

Three-Point Lighting: "Three-point lighting is the standard form of professional lighting in video production and still photography. It involves using three light sources placed in three different positions. It is a traditional method for illuminating a subject in a scene with light sources from three distinct positions."

    Key Light: The primary and brightest light source of the three lights. Placed typically slightly off the side of the camera at 45 degrees and the front of the object. 
    Fill Light: Mirrors the key light opposite of the camera. It fills in the shadows of the key light to the object. Typically darker than the key light.
    Back Light: The light that shines on the object from behind. 

Source: https://www.masterclass.com/articles/what-is-three-point-lighting-learn-about-the-lighting-technique-and-tips-for-the-best-three-point-lighting-setups 

# Functionality:
- Create a default L-shaped plane for the light to reflect
   1. Simply click on the 'Create Plane' button to create the default plane on your scene. Scale is set to 500 * 500 * 500 by default.
- Create Three Point Lighting on the Selected Object
   1. Select the object to apply lighting on
   2. Click on the 'Add Light' Button to apply three-point lighting on the object
   NOTE: Scale of the light will be dependent on the scale of the object.
- Change the Colour of the Back Light:
   The back light can be changed to any of these colours:
   <table>
  <tr>
    <th>Colour</th>
    <th>RGB Value</th>
  </tr>
  <tr>
    <td>Red</td>
    <td>(1, 0, 0)</td>
  </tr>
  <tr>
    <td>Blue</td>
    <td>(0, 1, 0)</td>
  </tr>
   <tr>
    <td>Green</td>
    <td>(0, 0, 1)</td>
  </tr>
  <tr>
    <td>Bright Red</td>
    <td>(1, 0.1, 0.1)</td>
  </tr>
  <tr>
    <td>Bright Green</td>
    <td>(0.5, 1, 0.1)</td>
  </tr>
  <tr>
    <td>Bright Blue</td>
    <td>(0.7, 1, 1)</td>
  </tr>
  <tr>
    <td>Orange</td>
    <td>(1, 0.5, 0)</td>
  </tr>
  <tr>
    <td>Pink</td>
    <td>(1, 0, 1)</td>
  </tr>
</table>

   1. Select your back light in the outliner
   2. Select your colour in the dropdown menu
   3. Confirm your settings by clicking on the 'Confirm Colour' button
   NOTE: It will raise an error if you chose another object that is not a back light
