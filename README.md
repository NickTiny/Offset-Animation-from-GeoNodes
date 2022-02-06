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

# Purpose
To explore methods of adjusting  and distributingh animated characters based on information retirived from Geomtry Nodes.

# Example Uses

Example with Characters

https://user-images.githubusercontent.com/86638335/152694291-57966f1a-99cc-4a64-be4f-c50f74cc1896.mp4





Example without Scale Random

![Example-Disable-Scale](https://user-images.githubusercontent.com/86638335/152693798-0f01d2f0-e012-4548-bda7-5294ccd1c7d0.gif)


Example with Scale Random

https://user-images.githubusercontent.com/86638335/152694302-cba6e0b9-ef2e-486d-9901-6e30159a9ada.mp4




Adjust layout with geomotry nodes.

![Change-Geo Nodes-Example](https://user-images.githubusercontent.com/86638335/152694192-fdb94ae7-3dad-4933-b46e-cff690f09883.gif)





# Next Steps
1. Replace with bpy.ops data blocks instead.
2. Update Math to allow for more control/variations.


# License
The code in this addon is licensed under the GNU General Public License, version 2.  Please see LICENSE_CODE.md for details.
