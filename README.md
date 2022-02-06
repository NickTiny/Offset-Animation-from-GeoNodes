# Offset-Animation-from-GeoNodes
Offset Animation from GeoNodes objects 

An addon for Blender that lets you distribute and offset the animations of characters from Geomotry Nodes Data.
This addon requires Blender 3.0+

![Example-Final-Product](https://user-images.githubusercontent.com/86638335/152693808-32e9d2d6-5ea0-4225-82e6-990ec366608b.gif)
# Release
 Download the [Latest Release](https://github.com/NickTiny/Offset-Animation-from-GeoNodes/releases/download/Pre-Release/Offset-GeoNodes-V-0-1.py)


# Usage
1. Create a Geomotry Nodes Object with a Captured Attribute
2. Set the Attribute to Position in the GN Modifier Panel
3. Select GN Object with "Target" selector.
4. Select Armature or any parent with "Source" selector
5. Run the "Offset from GeoNodes" Operator.

# Purpose
To explore methods of adjusting and distributing animated characters based on information retirived from Geomtry Nodes.

# Examples

Example with Characters

![Example-with-Characters](https://user-images.githubusercontent.com/86638335/152694387-7ae80235-0ddd-4845-9e95-feea2c560103.gif)


Example with Scale Random

![Random-Scale-Example](https://user-images.githubusercontent.com/86638335/152694401-8f2620b6-5839-4ae5-a282-756621dab635.gif)


Example without Scale Random

![Example-Disable-Scale](https://user-images.githubusercontent.com/86638335/152693798-0f01d2f0-e012-4548-bda7-5294ccd1c7d0.gif)

Adjust layout with geomotry nodes.

![Change-Geo Nodes-Example](https://user-images.githubusercontent.com/86638335/152694192-fdb94ae7-3dad-4933-b46e-cff690f09883.gif)





# Next Steps
1. Replace with bpy.ops data blocks instead.
2. Update Math to allow for more control/variations.


# License
The code in this addon is licensed under the GNU General Public License, version 2.  Please see LICENSE_CODE.md for details.
