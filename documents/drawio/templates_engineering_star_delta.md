---
title: "Star Delta Wireframe"
description: "A user interface wireframe showing layout and structure"
category: "templates/engineering"
type: "wireframe"
source_file: "templates/engineering/star_delta_decoded.xml"
---

# Star Delta Wireframe

A user interface wireframe showing layout and structure

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1408" dy="544" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1169" pageHeight="827" background="none" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="899" value="L1" style="text;align=center;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="138.5" y="169" width="40" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="900" value="F3" style="shape=mxgraph.electrical.miscellaneous.fuse_2;fillColor=white;strokeColor=#000000;direction=south;labelPosition=left;align=right;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="148.5" y="229" width="20" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="901" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;endArrow=none;rounded=0;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="900" target="899" edge="1">
      <mxGeometry x="478.5" y="199" width="100" height="100" as="geometry">
        <mxPoint x="478.5" y="299" as="sourcePoint"/>
        <mxPoint x="578.5" y="199" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="902" value="F2" style="shape=mxgraph.electrical.electro-mechanical.relay_contact_nc;fillColor=white;strokeColor=#000000;labelPosition=left;align=right;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="153.5" y="349" width="10" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="903" style="startArrow=none;endArrow=none;rounded=0;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="900" target="902" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="904" value="S1" style="shape=mxgraph.electrical.electro-mechanical.push_switch_nc;fillColor=white;strokeColor=#000000;direction=north;labelPosition=left;align=right;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="133.5" y="459" width="30" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="905" style="entryX=1;entryY=0.835;entryPerimeter=0;exitX=0.5;exitY=1;exitPerimeter=0;endArrow=none;rounded=0;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="902" target="904" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="348.5" y="499" as="sourcePoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="906" value="S2" style="shape=mxgraph.electrical.electro-mechanical.push_switch_no;fillColor=white;strokeColor=#000000;direction=north;fontStyle=1;labelPosition=left;align=right;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="133.5" y="609" width="30" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="907" style="exitX=0;exitY=0.835;exitPerimeter=0;entryX=1;entryY=0.835;entryPerimeter=0;endArrow=none;rounded=0;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="904" target="906" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="908" value="K2" style="shape=mxgraph.electrical.electro-mechanical.relay_contact_nc;fillColor=white;strokeColor=#000000;fontStyle=1;labelPosition=left;align=right;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="153.5" y="739" width="10" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="909" style="exitX=0;exitY=0.835;exitPerimeter=0;entryX=0.5;entryY=0;entryPerimeter=0;endArrow=none;rounded=0;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="906" target="908" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="910" value="K3" style="shape=mxgraph.electrical.electro-mechanical.relay_contact_nc;fillColor=white;strokeColor=#000000;fontStyle=1;labelPosition=left;align=right;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="153.5" y="1039" width="10" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="911" value="K1" style="shape=mxgraph.electrical.electro-mechanical.relay_coil;fillColor=white;strokeColor=#000000;fontStyle=1;labelPosition=left;align=right;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="109" y="1239" width="99" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="912" style="exitX=0.5;exitY=0;exitPerimeter=0;entryX=0.5;entryY=1;entryPerimeter=0;rounded=0;endArrow=none;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="910" target="908" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="913" style="exitX=0.5;exitY=1;exitPerimeter=0;entryX=0.5;entryY=0;entryPerimeter=0;rounded=0;endArrow=none;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="910" target="911" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="914" value="K1T" style="shape=mxgraph.electrical.electro-mechanical.relay_coil;fillColor=white;strokeColor=#000000;fontStyle=1;labelPosition=left;align=right;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="258.5" y="1239" width="99" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="915" value="K3" style="shape=mxgraph.electrical.electro-mechanical.relay_coil;fillColor=white;strokeColor=#000000;fontStyle=1;labelPosition=left;align=right;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="418.5" y="1239" width="99" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="916" value="K2" style="shape=mxgraph.electrical.electro-mechanical.relay_coil;fillColor=white;strokeColor=#000000;fontStyle=1;labelPosition=left;align=right;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="698.5" y="1239" width="99" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="917" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0.5;exitY=0;exitPerimeter=0;rounded=0;endArrow=none;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="914" edge="1">
      <mxGeometry x="338.5" y="1039" width="100" height="100" as="geometry">
        <mxPoint x="338.5" y="1139" as="sourcePoint"/>
        <mxPoint x="158.5" y="1189" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="248.5" y="1189"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="918" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;rounded=0;endArrow=none;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" edge="1">
      <mxGeometry x="513" y="1038.5" width="100" height="100" as="geometry">
        <mxPoint x="83" y="1338.5" as="sourcePoint"/>
        <mxPoint x="853" y="1338.5" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="919" value="K1" style="shape=mxgraph.electrical.electro-mechanical.relay_contact_nc;fillColor=white;strokeColor=#000000;fontStyle=1;labelPosition=left;align=right;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="463" y="1049" width="10" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="920" value="K1T" style="shape=mxgraph.electrical.electro-mechanical.relay_contact_nc;fillColor=white;strokeColor=#000000;fontStyle=1;labelPosition=left;align=right;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="598.5" y="1049" width="10" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="921" value="K1" style="shape=mxgraph.electrical.electro-mechanical.relay_contact_no;fillColor=white;strokeColor=#000000;fontStyle=1;labelPosition=left;align=right;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="463" y="919" width="20" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="922" value="K2" style="shape=mxgraph.electrical.electro-mechanical.relay_contact_no;fillColor=white;strokeColor=#000000;fontStyle=1;labelPosition=left;align=right;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="743" y="919" width="20" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="923" value="K1" style="shape=mxgraph.electrical.electro-mechanical.relay_contact_no;fillColor=white;strokeColor=#000000;fontStyle=1;labelPosition=left;align=right;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="858.5" y="919" width="20" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="924" value="" style="edgeStyle=none;exitX=0.5;exitY=1;exitPerimeter=0;entryX=0.5;entryY=0;entryPerimeter=0;rounded=0;endArrow=none;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" edge="1">
      <mxGeometry x="58.5" y="139" width="100" height="100" as="geometry">
        <mxPoint x="468.1666666666665" y="1149" as="sourcePoint"/>
        <mxPoint x="468.1666666666665" y="1239" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="925" value="" style="edgeStyle=none;exitX=0.5;exitY=0;exitPerimeter=0;entryX=0.25;entryY=1;entryPerimeter=0;rounded=0;endArrow=none;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="919" target="921" edge="1">
      <mxGeometry x="58.5" y="139" width="100" height="100" as="geometry">
        <mxPoint x="58.5" y="239" as="sourcePoint"/>
        <mxPoint x="158.5" y="139" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="926" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0.25;exitY=0;exitPerimeter=0;rounded=0;endArrow=none;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="921" edge="1">
      <mxGeometry x="358.5" y="709" width="100" height="100" as="geometry">
        <mxPoint x="358.5" y="809" as="sourcePoint"/>
        <mxPoint x="158.5" y="879" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="318.5" y="879"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="927" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0.5;exitY=0;exitPerimeter=0;rounded=0;endArrow=none;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="920" edge="1">
      <mxGeometry x="558.5" y="829" width="100" height="100" as="geometry">
        <mxPoint x="558.5" y="929" as="sourcePoint"/>
        <mxPoint x="468.5" y="1039" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="538.5" y="1039"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="928" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0.5;exitY=0;exitPerimeter=0;entryX=0.25;entryY=1;entryPerimeter=0;rounded=0;endArrow=none;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="916" target="922" edge="1">
      <mxGeometry x="58.5" y="139" width="100" height="100" as="geometry">
        <mxPoint x="58.5" y="239" as="sourcePoint"/>
        <mxPoint x="158.5" y="139" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="929" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0.25;exitY=1;exitPerimeter=0;entryX=0.5;entryY=0;entryPerimeter=0;rounded=0;endArrow=none;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="923" target="916" edge="1">
      <mxGeometry x="58.5" y="139" width="100" height="100" as="geometry">
        <mxPoint x="58.5" y="239" as="sourcePoint"/>
        <mxPoint x="158.5" y="139" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="808.5" y="1199"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="930" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0.5;exitY=1;exitPerimeter=0;entryX=0.5;entryY=0;entryPerimeter=0;rounded=0;endArrow=none;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="920" target="916" edge="1">
      <mxGeometry x="58.5" y="139" width="100" height="100" as="geometry">
        <mxPoint x="58.5" y="239" as="sourcePoint"/>
        <mxPoint x="158.5" y="139" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="688.5" y="1199"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="931" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0.25;exitY=0;exitPerimeter=0;rounded=0;endArrow=none;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="922" edge="1">
      <mxGeometry x="548.5" y="599" width="100" height="100" as="geometry">
        <mxPoint x="548.5" y="699" as="sourcePoint"/>
        <mxPoint x="158.5" y="579" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="448.5" y="579"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="932" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0.25;exitY=0;exitPerimeter=0;rounded=0;endArrow=none;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="923" edge="1">
      <mxGeometry x="898.5" y="639" width="100" height="100" as="geometry">
        <mxPoint x="898.5" y="739" as="sourcePoint"/>
        <mxPoint x="748.5" y="579" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="818.5" y="579"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="933" value="1" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="158.5" y="219" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="934" value="2" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="158.5" y="309" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="935" value="55" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="158.5" y="339" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="936" value="56" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="158.5" y="429" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="937" value="21" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="158.5" y="449" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="938" value="22" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="158.5" y="539" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="939" value="13" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="158.5" y="599" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="940" value="14" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="158.5" y="689" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="941" value="22" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="158.5" y="819" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="942" value="21" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="158.5" y="729" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="943" value="21" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="158.5" y="1029" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="944" value="22" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="158.5" y="1123" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="945" value="43" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="468" y="909" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="946" value="44" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="468" y="1003" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="947" value="21" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="468" y="1039" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="948" value="22" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="468" y="1133" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="949" value="15" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="603.5" y="1042" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="950" value="16" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="603.5" y="1133" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="951" value="13" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="748" y="909" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="952" value="14" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="748" y="1003" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="953" value="13" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="868.5" y="909" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="954" value="14" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="868.5" y="1003" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="955" value="A1" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="158.5" y="1255" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="956" value="A1" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="308" y="1255" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="957" value="A1" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="468" y="1255" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="958" value="A1" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="748" y="1255" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="959" value="A2" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="158.5" y="1297" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="960" value="A2" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="308" y="1297" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="961" value="A2" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="468" y="1297" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="962" value="A2" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="748" y="1297" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="963" value="N" style="text;align=left;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="79" y="1315" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="964" value="N" style="text;align=left;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="818.5" y="1313" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="965" value="star" style="text;align=center;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="128.5" y="1356" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="966" value="delta" style="text;align=center;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="438" y="1356" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="967" value="motor" style="text;align=center;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="718" y="1356" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="968" value="Control circuit diagram" style="text;align=center;fontSize=24;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="163.5" y="1449" width="625" height="36" as="geometry"/>
    </mxCell>
    <mxCell id="969" value="M&#10;3~" style="shape=mxgraph.bpmn.general_start;fillColor=white;strokeColor=#000000;strokeWidth=2;perimeter=ellipsePerimeter;fontSize=24;fontStyle=1;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1598.5" y="1225.5" width="99" height="99" as="geometry"/>
    </mxCell>
    <mxCell id="970" value="F1" style="shape=mxgraph.electrical.miscellaneous.fuse_2;fillColor=white;strokeColor=#000000;direction=south;labelPosition=left;align=right;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1308.5" y="515" width="20" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="971" value="" style="shape=mxgraph.electrical.miscellaneous.fuse_2;fillColor=white;strokeColor=#000000;direction=south;labelPosition=left;align=right;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1368.5" y="515" width="20" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="972" value="" style="shape=mxgraph.electrical.miscellaneous.fuse_2;fillColor=white;strokeColor=#000000;direction=south;labelPosition=left;align=right;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1428.5" y="515" width="20" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="973" value="K2" style="shape=mxgraph.electrical.electro-mechanical.relay_contact_no;fillColor=white;strokeColor=#000000;fontStyle=1;labelPosition=left;align=right;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1313.5" y="742" width="20" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="974" value="" style="shape=mxgraph.electrical.electro-mechanical.relay_contact_no;fillColor=white;strokeColor=#000000;fontStyle=1;labelPosition=left;align=right;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1373.5" y="739" width="20" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="975" value="" style="shape=mxgraph.electrical.electro-mechanical.relay_contact_no;fillColor=white;strokeColor=#000000;fontStyle=1;labelPosition=left;align=right;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1433.5" y="739" width="20" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="976" value="F2" style="shape=mxgraph.electrical.electro-mechanical.relay_coil;fillColor=white;strokeColor=#000000;fontStyle=1;labelPosition=left;align=right;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1289" y="899" width="59" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="977" value="" style="shape=mxgraph.electrical.electro-mechanical.relay_coil;fillColor=white;strokeColor=#000000;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1349" y="899" width="59" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="978" value="" style="shape=mxgraph.electrical.electro-mechanical.relay_coil;fillColor=white;strokeColor=#000000;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1409" y="899" width="59" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="979" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0.25;exitY=0;exitPerimeter=0;entryX=1;entryY=0.5;entryPerimeter=0;rounded=0;endArrow=none;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="973" target="970" edge="1">
      <mxGeometry x="58.5" y="139" width="100" height="100" as="geometry">
        <mxPoint x="58.5" y="239" as="sourcePoint"/>
        <mxPoint x="158.5" y="139" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="980" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=1;exitY=0.5;exitPerimeter=0;entryX=0.25;entryY=0;entryPerimeter=0;rounded=0;endArrow=none;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="971" target="974" edge="1">
      <mxGeometry x="58.5" y="139" width="100" height="100" as="geometry">
        <mxPoint x="58.5" y="239" as="sourcePoint"/>
        <mxPoint x="158.5" y="139" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="981" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=1;exitY=0.5;exitPerimeter=0;entryX=0.25;entryY=0;entryPerimeter=0;rounded=0;endArrow=none;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="972" target="975" edge="1">
      <mxGeometry x="58.5" y="139" width="100" height="100" as="geometry">
        <mxPoint x="58.5" y="239" as="sourcePoint"/>
        <mxPoint x="158.5" y="139" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="982" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0.25;exitY=1;exitPerimeter=0;entryX=0.5;entryY=0;entryPerimeter=0;rounded=0;endArrow=none;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="975" target="978" edge="1">
      <mxGeometry x="58.5" y="139" width="100" height="100" as="geometry">
        <mxPoint x="58.5" y="239" as="sourcePoint"/>
        <mxPoint x="158.5" y="139" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="983" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0.25;exitY=1;exitPerimeter=0;entryX=0.5;entryY=0;entryPerimeter=0;rounded=0;endArrow=none;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="974" target="977" edge="1">
      <mxGeometry x="58.5" y="139" width="100" height="100" as="geometry">
        <mxPoint x="58.5" y="239" as="sourcePoint"/>
        <mxPoint x="158.5" y="139" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="984" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0.25;exitY=1;exitPerimeter=0;entryX=0.5;entryY=0;entryPerimeter=0;rounded=0;endArrow=none;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="973" target="976" edge="1">
      <mxGeometry x="58.5" y="139" width="100" height="100" as="geometry">
        <mxPoint x="58.5" y="239" as="sourcePoint"/>
        <mxPoint x="158.5" y="139" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="985" value="" style="shape=mxgraph.electrical.electro-mechanical.relay_contact_no;fillColor=white;strokeColor=#000000;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1548.5" y="899" width="20" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="986" value="" style="shape=mxgraph.electrical.electro-mechanical.relay_contact_nc;fillColor=white;strokeColor=#000000;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1618.5" y="899" width="10" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="987" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;rounded=0;endArrow=none;dashed=1;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="978" edge="1">
      <mxGeometry x="358" y="186" width="100" height="100" as="geometry">
        <mxPoint x="1618" y="789" as="sourcePoint"/>
        <mxPoint x="1628.5" y="949" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="988" value="" style="edgeStyle=segmentEdgeStyle;exitX=0.145;exitY=0.145;exitPerimeter=0;entryX=0.5;entryY=1;entryPerimeter=0;rounded=0;endArrow=none;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="969" target="978" edge="1">
      <mxGeometry x="58.5" y="139" width="100" height="100" as="geometry">
        <mxPoint x="58.5" y="239" as="sourcePoint"/>
        <mxPoint x="158.5" y="139" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="989" value="" style="edgeStyle=segmentEdgeStyle;exitX=0;exitY=0.5;exitPerimeter=0;entryX=0.5;entryY=1;entryPerimeter=0;rounded=0;endArrow=none;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="969" target="977" edge="1">
      <mxGeometry x="58.5" y="139" width="100" height="100" as="geometry">
        <mxPoint x="58.5" y="239" as="sourcePoint"/>
        <mxPoint x="158.5" y="139" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="990" value="" style="edgeStyle=segmentEdgeStyle;exitX=0.145;exitY=0.855;exitPerimeter=0;entryX=0.5;entryY=1;entryPerimeter=0;rounded=0;endArrow=none;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="969" target="976" edge="1">
      <mxGeometry x="58.5" y="139" width="100" height="100" as="geometry">
        <mxPoint x="58.5" y="239" as="sourcePoint"/>
        <mxPoint x="158.5" y="139" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="991" value="K3" style="shape=mxgraph.electrical.electro-mechanical.relay_contact_no;fillColor=white;strokeColor=#000000;fontStyle=1;labelPosition=left;align=right;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1778.5" y="750.5" width="20" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="992" value="" style="shape=mxgraph.electrical.electro-mechanical.relay_contact_no;fillColor=white;strokeColor=#000000;fontStyle=1;labelPosition=left;align=right;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1838.5" y="747.5" width="20" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="993" value="" style="shape=mxgraph.electrical.electro-mechanical.relay_contact_no;fillColor=white;strokeColor=#000000;fontStyle=1;labelPosition=left;align=right;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1898.5" y="747.5" width="20" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="994" value="" style="edgeStyle=segmentEdgeStyle;exitX=0.25;exitY=0;exitPerimeter=0;rounded=0;endArrow=none;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="991" edge="1">
      <mxGeometry x="1698.5" y="459" width="100" height="100" as="geometry">
        <mxPoint x="1698.5" y="559" as="sourcePoint"/>
        <mxPoint x="1318.5" y="709" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="1783.5" y="709"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="995" value="" style="edgeStyle=segmentEdgeStyle;exitX=0.25;exitY=0;exitPerimeter=0;rounded=0;endArrow=none;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="992" edge="1">
      <mxGeometry x="1898.5" y="459" width="100" height="100" as="geometry">
        <mxPoint x="1898.5" y="559" as="sourcePoint"/>
        <mxPoint x="1378.5" y="669" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="1843.5" y="669"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="996" value="" style="edgeStyle=segmentEdgeStyle;exitX=0.25;exitY=0;exitPerimeter=0;rounded=0;endArrow=none;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="993" edge="1">
      <mxGeometry x="2088.5" y="469" width="100" height="100" as="geometry">
        <mxPoint x="2088.5" y="569" as="sourcePoint"/>
        <mxPoint x="1438.5" y="619" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="1903.5" y="619"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="997" value="K1" style="shape=mxgraph.electrical.electro-mechanical.relay_contact_no;fillColor=white;strokeColor=#000000;fontStyle=1;labelPosition=left;align=right;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="2068.5" y="748.9999999999998" width="20" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="998" value="" style="shape=mxgraph.electrical.electro-mechanical.relay_contact_no;fillColor=white;strokeColor=#000000;fontStyle=1;labelPosition=left;align=right;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="2128.5" y="745.9999999999998" width="20" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="999" value="" style="shape=mxgraph.electrical.electro-mechanical.relay_contact_no;fillColor=white;strokeColor=#000000;fontStyle=1;labelPosition=left;align=right;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="2188.5" y="745.9999999999998" width="20" height="100" as="geometry"/>
    </mxCell>
    <mxCell id="1000" value="" style="edgeStyle=segmentEdgeStyle;exitX=0.25;exitY=1;exitPerimeter=0;entryX=0.855;entryY=0.145;entryPerimeter=0;rounded=0;endArrow=none;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="991" target="969" edge="1">
      <mxGeometry x="58.5" y="139" width="100" height="100" as="geometry">
        <mxPoint x="58.5" y="239" as="sourcePoint"/>
        <mxPoint x="158.5" y="139" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="1782.5" y="851"/>
          <mxPoint x="1782.5" y="1240"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="1001" value="" style="edgeStyle=segmentEdgeStyle;exitX=0.25;exitY=1;exitPerimeter=0;entryX=0.855;entryY=0.855;entryPerimeter=0;rounded=0;endArrow=none;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="992" target="969" edge="1">
      <mxGeometry x="58.5" y="139" width="100" height="100" as="geometry">
        <mxPoint x="58.5" y="239" as="sourcePoint"/>
        <mxPoint x="158.5" y="139" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="1843.5" y="1310"/>
          <mxPoint x="1683.5" y="1310"/>
          <mxPoint x="1683.5" y="1310"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="1002" value="" style="edgeStyle=segmentEdgeStyle;exitX=0.25;exitY=1;exitPerimeter=0;entryX=1;entryY=0.5;entryPerimeter=0;rounded=0;endArrow=none;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="993" target="969" edge="1">
      <mxGeometry x="58.5" y="139" width="100" height="100" as="geometry">
        <mxPoint x="58.5" y="239" as="sourcePoint"/>
        <mxPoint x="158.5" y="139" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="1903.5" y="1275"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="1003" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0.25;exitY=1;exitPerimeter=0;rounded=0;endArrow=none;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="997" edge="1">
      <mxGeometry x="2069.5" y="994" width="100" height="100" as="geometry">
        <mxPoint x="2069.5" y="1094" as="sourcePoint"/>
        <mxPoint x="1782.8595679012346" y="928.2708333333335" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="1928.5" y="928"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="1004" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0.25;exitY=1;exitPerimeter=0;rounded=0;endArrow=none;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="998" edge="1">
      <mxGeometry x="2281.5" y="990" width="100" height="100" as="geometry">
        <mxPoint x="2281.5" y="1090" as="sourcePoint"/>
        <mxPoint x="1843.1412037037035" y="980.8364197530864" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="1995.5" y="981"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="1005" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0.25;exitY=1;exitPerimeter=0;rounded=0;endArrow=none;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="999" edge="1">
      <mxGeometry x="2267.5" y="694" width="100" height="100" as="geometry">
        <mxPoint x="2267.5" y="794" as="sourcePoint"/>
        <mxPoint x="1902.9405864197533" y="1023.7569444444443" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="2059.5" y="1024"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="1006" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;exitX=0.25;exitY=0;exitPerimeter=0;entryX=0.25;entryY=0;entryPerimeter=0;rounded=0;endArrow=none;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="999" target="997" edge="1">
      <mxGeometry x="2238.5" y="647.5" width="100" height="100" as="geometry">
        <mxPoint x="2238.5" y="747.5" as="sourcePoint"/>
        <mxPoint x="2300.5" y="1081" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="2128.5" y="696"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="1007" value="" style="edgeStyle=none;exitX=0.25;exitY=0;exitPerimeter=0;rounded=0;endArrow=none;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" source="998" edge="1">
      <mxGeometry x="2068.835648148148" y="547.2908950617284" width="100" height="100" as="geometry">
        <mxPoint x="2068.835648148148" y="647.2908950617284" as="sourcePoint"/>
        <mxPoint x="2132.9753086419755" y="698.2361111111111" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="1008" value="L1" style="text;align=center;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1298.5" y="489" width="40" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1009" value="L2" style="text;align=center;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1358.5" y="489" width="40" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1010" value="L3" style="text;align=center;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1418.5" y="489" width="40" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1011" value="W1" style="text;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1568.5" y="1212.5" width="40" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1012" value="V1" style="text;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1558.5" y="1248.5" width="40" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1013" value="U1" style="text;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1568.5" y="1281.5" width="40" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1014" value="W2" style="text;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1684.5" y="1212.5" width="40" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1015" value="V2" style="text;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1704.5000000000005" y="1248.4999999999998" width="40" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1016" value="U2" style="text;fontStyle=1;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1697.5" y="1281.5" width="40" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1017" value="M1" style="text;fontStyle=1;fontSize=14;align=center;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1628" y="1339" width="40" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1018" value="1" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1319" y="509" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1019" value="2" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1318" y="596" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1020" value="3" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1378" y="509" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1021" value="4" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1378" y="596" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1022" value="5" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1438" y="509" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1023" value="6" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1438" y="596" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1024" value="1" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="1319" y="732" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1025" value="3" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="1378" y="732" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1026" value="5" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="1438" y="732" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1027" value="2" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="1318" y="819" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1028" value="4" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="1378" y="819" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1029" value="6" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="1438" y="819" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1030" value="1" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1320" y="892.5" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1031" value="3" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1379" y="892.5" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1032" value="5" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1439" y="892.5" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1033" value="2" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1319" y="979.5" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1034" value="4" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1379" y="979.5" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1035" value="6" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1439" y="979.5" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1036" value="1" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="1789.5" y="741" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1037" value="3" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="1848.5" y="741" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1038" value="5" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="1908.5" y="741" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1039" value="2" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="1788.5" y="828" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1040" value="4" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="1848.5" y="828" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1041" value="6" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="1908.5" y="828" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1042" value="1" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="2079.5" y="741" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1043" value="3" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="2138.5" y="741" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1044" value="5" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="2198.5" y="741" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1045" value="2" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="2078.5" y="828" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1046" value="4" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="2138.5" y="828" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1047" value="6" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;strokeColor=none;" parent="1" vertex="1">
      <mxGeometry x="2198.5" y="828" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1048" value="97" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1558.5" y="892.5" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1049" value="95" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1628" y="892.5" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1050" value="98" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1557.5" y="979.5" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1051" value="96" style="text;align=left;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1628.5" y="979.5" width="60" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="1052" value="" style="edgeStyle=none;endArrow=none;dashed=1;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" edge="1">
      <mxGeometry x="1343.5000000000002" y="791.6527777777777" width="100" height="100" as="geometry">
        <mxPoint x="1323.5" y="791.6527777777778" as="sourcePoint"/>
        <mxPoint x="1443.5" y="791.6527777777778" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="1053" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;rounded=0;endArrow=none;dashed=1;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" edge="1">
      <mxGeometry x="709.4999999999998" y="45.47222222222169" width="100" height="100" as="geometry">
        <mxPoint x="1789.5" y="800.7361111111109" as="sourcePoint"/>
        <mxPoint x="1909.5" y="800.7361111111109" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="1054" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;rounded=0;endArrow=none;dashed=1;strokeWidth=2;html=1;fontColor=#000000;strokeColor=#000000;" parent="1" edge="1">
      <mxGeometry x="999.5" y="44.88888888888859" width="100" height="100" as="geometry">
        <mxPoint x="2079.5" y="800.1527777777778" as="sourcePoint"/>
        <mxPoint x="2199.5" y="800.1527777777778" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="1055" value="Power circuit diagram" style="text;align=center;fontSize=24;strokeWidth=2;html=1;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="1335.5" y="1449" width="625" height="36" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>

```
