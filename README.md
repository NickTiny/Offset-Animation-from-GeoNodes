# Offset-Animation-from-GeoNodes
Offset Animation from GeoNodes objects

An addon for Blender that lets you distribute and offset the animations of characters from Geomotry Nodes Data.
This addon requires Blender 3.0.0 or later.

![Example-Final-Product](https://user-images.githubusercontent.com/86638335/152693808-32e9d2d6-5ea0-4225-82e6-990ec366608b.gif)

# Usage
1. Create a Geomotry Nodes Object with a Captured Attribute
2. Set the Attribute to Position in the GN Modifier Panel
3. Select GN Object with "Target" selector.
4. Select Armature or any parent with "Source" selector
5. Run the "Offset from GeoNodes" Operator.

# Example Uses

Example with Characters
![Example-with-Characters](https://user-images.githubusercontent.com/86638335/152693791-eeaa6ed3-e8be-4c20-81d8-a2d1cfa22c11.gif)

Example with no Scale Randmoization
![Example-Disable-Scale](https://user-images.githubusercontent.com/86638335/152693798-0f01d2f0-e012-4548-bda7-5294ccd1c7d0.gif)

Example with Scale Randmoization
![Change-Geo Nodes-Example](https://user-images.githubusercontent.com/86638335/152693803-d5e79902-bac3-40f9-8f23-de6b6a2e757f.gif)




# Next Steps
1. Replace with bpy.ops data blocks instead.
2. Update Math to allow for more control/variations.


# License
The code in this addon is licensed under the GNU General Public License, version 2.  Please see LICENSE_CODE.md for details.
