---

---

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="738" dy="1146" grid="0" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="826" pageHeight="1169" background="#ffffff" math="0" shadow="1">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="2" value="" style="rounded=0;html=1;jettySize=auto;orthogonalLoop=1;fontSize=11;endArrow=block;endFill=0;endSize=8;strokeWidth=1;shadow=0;labelBackgroundColor=none;" parent="1" source="3" target="6" edge="1">
      <mxGeometry x="340" y="120" as="geometry"/>
    </mxCell>
    <object label="Lamp doesn't work" Condition="Lamp does not produce light." id="3">
      <mxCell style="rounded=1;whiteSpace=wrap;html=1;fontSize=12;plain-red;glass=1;strokeWidth=1;shadow=0;" parent="1" vertex="1">
        <mxGeometry x="280" y="80" width="120" height="40" as="geometry"/>
      </mxCell>
    </object>
    <mxCell id="4" value="Yes" style="rounded=0;html=1;jettySize=auto;orthogonalLoop=1;fontSize=11;endArrow=block;endFill=0;endSize=8;strokeWidth=1;shadow=0;labelBackgroundColor=none;" parent="1" source="6" target="10" edge="1">
      <mxGeometry x="340" y="250" as="geometry">
        <mxPoint as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="5" value="No" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;fontSize=11;endArrow=block;endFill=0;endSize=8;strokeWidth=1;shadow=0;labelBackgroundColor=none;" parent="1" source="6" target="7" edge="1">
      <mxGeometry x="390" y="210" as="geometry">
        <mxPoint as="offset"/>
      </mxGeometry>
    </mxCell>
    <object label="Lamp&lt;br&gt;plugged in?" Condition="Lamp connected to power outlet?" id="6">
      <mxCell style="rhombus;whiteSpace=wrap;html=1;shadow=0;fontFamily=Helvetica;fontSize=12;fontColor=#000000;align=center;strokeColor=#D6B656;strokeWidth=1;fillColor=#FFF2CC;gradientColor=#FFD966;spacing=6;spacingTop=-4;" parent="1" vertex="1">
        <mxGeometry x="290" y="170" width="100" height="80" as="geometry"/>
      </mxCell>
    </object>
    <object label="Plug in lamp" Action="Connect lamp to power outlet." id="7">
      <mxCell style="rounded=1;whiteSpace=wrap;html=1;fontSize=12;plain-green;glass=1;strokeWidth=1;shadow=0;" parent="1" vertex="1">
        <mxGeometry x="440" y="190" width="120" height="40" as="geometry"/>
      </mxCell>
    </object>
    <mxCell id="8" value="No" style="rounded=0;html=1;jettySize=auto;orthogonalLoop=1;fontSize=11;endArrow=block;endFill=0;endSize=8;strokeWidth=1;shadow=0;labelBackgroundColor=none;" parent="1" source="10" target="11" edge="1">
      <mxGeometry x="340" y="370" as="geometry">
        <mxPoint as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="9" value="Yes" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;fontSize=11;endArrow=block;endFill=0;endSize=8;strokeWidth=1;shadow=0;labelBackgroundColor=none;" parent="1" source="10" target="12" edge="1">
      <mxGeometry x="390" y="330" as="geometry">
        <mxPoint as="offset"/>
      </mxGeometry>
    </mxCell>
    <object label="Bulb&lt;br&gt;burned out?" Condition="Check if bulb is broken." id="10">
      <mxCell style="rhombus;whiteSpace=wrap;html=1;shadow=0;fontFamily=Helvetica;fontSize=12;fontColor=#000000;align=center;strokeColor=#D6B656;strokeWidth=1;fillColor=#FFF2CC;gradientColor=#FFD966;spacing=6;spacingTop=-4;" parent="1" vertex="1">
        <mxGeometry x="290" y="290" width="100" height="80" as="geometry"/>
      </mxCell>
    </object>
    <object label="Repair Lamp" Action="Repair other parts of lamp." id="11">
      <mxCell style="rounded=1;whiteSpace=wrap;html=1;fontSize=12;plain-green;glass=1;strokeWidth=1;shadow=0;" parent="1" vertex="1">
        <mxGeometry x="280" y="410" width="120" height="40" as="geometry"/>
      </mxCell>
    </object>
    <object label="Replace Bulb" Action="Get new bulb and replace existing bulb." id="12">
      <mxCell style="rounded=1;whiteSpace=wrap;html=1;fontSize=12;plain-green;glass=1;strokeWidth=1;shadow=0;" parent="1" vertex="1">
        <mxGeometry x="440" y="310" width="120" height="40" as="geometry"/>
      </mxCell>
    </object>
  </root>
</mxGraphModel>
```