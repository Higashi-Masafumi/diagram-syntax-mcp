---
title: "Bpmn 3 Flowchart"
description: "A flowchart diagram showing process flow and decision points"
category: "templates/business"
type: "flowchart"
source_file: "templates/business/bpmn_3_decoded.xml"
tags: ["process", "bpmn", "template", "business", "business_process", "drawio", "workflow"]
---

# Bpmn 3 Flowchart

A flowchart diagram showing process flow and decision points

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1408" dy="544" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" background="none" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="7a84cebc1def654-1" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=ellipsePerimeter;outline=standard;symbol=general;" parent="1" vertex="1">
      <mxGeometry x="260" y="265" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-2" value="Task" style="shape=ext;rounded=1;html=1;whiteSpace=wrap;" parent="1" vertex="1">
      <mxGeometry x="360" y="250" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-3" value="Task" style="shape=ext;rounded=1;html=1;whiteSpace=wrap;" parent="1" vertex="1">
      <mxGeometry x="530" y="250" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-4" value="" style="shape=message;whiteSpace=wrap;html=1;" parent="1" vertex="1">
      <mxGeometry x="400" y="175" width="40" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-5" value="" style="shape=message;whiteSpace=wrap;html=1;" parent="1" vertex="1">
      <mxGeometry x="570" y="175" width="40" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-6" value="" style="shape=hexagon;whiteSpace=wrap;html=1;perimeter=hexagonPerimeter;" parent="1" vertex="1">
      <mxGeometry x="560" y="375" width="60" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-7" value="" style="html=1;shape=plus;" parent="7a84cebc1def654-6" vertex="1">
      <mxGeometry x="0.5" y="1" width="14" height="14" relative="1" as="geometry">
        <mxPoint x="-7" y="-14" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="7a84cebc1def654-8" value="Task" style="shape=ext;rounded=1;html=1;whiteSpace=wrap;" parent="1" vertex="1">
      <mxGeometry x="530" y="475" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-9" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=rhombusPerimeter;background=gateway;outline=none;symbol=parallelGw;" parent="1" vertex="1">
      <mxGeometry x="695" y="490" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-12" value="Sub-Process" style="html=1;whiteSpace=wrap;rounded=1;" parent="1" vertex="1">
      <mxGeometry x="970" y="250" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-13" value="" style="html=1;shape=plus;" parent="7a84cebc1def654-12" vertex="1">
      <mxGeometry x="0.5" y="1" width="14" height="14" relative="1" as="geometry">
        <mxPoint x="-7" y="-14" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="7a84cebc1def654-14" value="Receive" style="html=1;whiteSpace=wrap;rounded=1;" parent="1" vertex="1">
      <mxGeometry x="780" y="250" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-15" value="" style="html=1;shape=message;" parent="7a84cebc1def654-14" vertex="1">
      <mxGeometry width="20" height="14" relative="1" as="geometry">
        <mxPoint x="7" y="7" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="7a84cebc1def654-16" value="Process" style="html=1;whiteSpace=wrap;rounded=1;" parent="1" vertex="1">
      <mxGeometry x="905" y="475" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-17" value="" style="shape=mxgraph.bpmn.timer_start;perimeter=ellipsePerimeter;html=1;labelPosition=right;labelBackgroundColor=#ffffff;align=left;" parent="7a84cebc1def654-16" vertex="1">
      <mxGeometry x="1" width="30" height="30" relative="1" as="geometry">
        <mxPoint x="-15" y="10" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="7a84cebc1def654-18" value="Process" style="html=1;whiteSpace=wrap;rounded=1;" parent="1" vertex="1">
      <mxGeometry x="1220" y="775" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-19" value="" style="shape=mxgraph.bpmn.timer_start;perimeter=ellipsePerimeter;html=1;labelPosition=right;labelBackgroundColor=#ffffff;align=left;" parent="7a84cebc1def654-18" vertex="1">
      <mxGeometry x="1" width="30" height="30" relative="1" as="geometry">
        <mxPoint x="-15" y="10" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="7a84cebc1def654-20" value="Receive" style="html=1;whiteSpace=wrap;rounded=1;" parent="1" vertex="1">
      <mxGeometry x="1050" y="775" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-21" value="" style="html=1;shape=message;" parent="7a84cebc1def654-20" vertex="1">
      <mxGeometry width="20" height="14" relative="1" as="geometry">
        <mxPoint x="7" y="7" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="7a84cebc1def654-22" value="Sub-Process" style="html=1;whiteSpace=wrap;rounded=1;" parent="1" vertex="1">
      <mxGeometry x="905" y="775" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-23" value="" style="html=1;shape=plus;" parent="7a84cebc1def654-22" vertex="1">
      <mxGeometry x="0.5" y="1" width="14" height="14" relative="1" as="geometry">
        <mxPoint x="-7" y="-14" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="7a84cebc1def654-24" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=rhombusPerimeter;background=gateway;outline=none;symbol=parallelGw;" parent="1" vertex="1">
      <mxGeometry x="1255" y="490" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-26" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=ellipsePerimeter;outline=end;symbol=general;" parent="1" vertex="1">
      <mxGeometry x="1390" y="490.00000000000006" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-27" value="" style="shape=message;whiteSpace=wrap;html=1;" parent="1" vertex="1">
      <mxGeometry x="820" y="175" width="40" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-28" value="" style="shape=message;whiteSpace=wrap;html=1;" parent="1" vertex="1">
      <mxGeometry x="1010" y="175" width="40" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-29" value="Sub-Process" style="html=1;whiteSpace=wrap;rounded=1;" parent="1" vertex="1">
      <mxGeometry x="660" y="655" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-30" value="" style="html=1;shape=plus;" parent="7a84cebc1def654-29" vertex="1">
      <mxGeometry x="0.5" y="1" width="14" height="14" relative="1" as="geometry">
        <mxPoint x="-7" y="-14" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="7a84cebc1def654-31" value="" style="shape=message;whiteSpace=wrap;html=1;" parent="1" vertex="1">
      <mxGeometry x="700" y="775" width="40" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-32" value="" style="shape=message;whiteSpace=wrap;html=1;" parent="1" vertex="1">
      <mxGeometry x="1090" y="895" width="40" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-33" value="" style="shape=message;whiteSpace=wrap;html=1;" parent="1" vertex="1">
      <mxGeometry x="1260" y="895" width="40" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-34" value="" style="shape=message;whiteSpace=wrap;html=1;" parent="1" vertex="1">
      <mxGeometry x="945" y="895" width="40" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-35" value="" style="shape=message;whiteSpace=wrap;html=1;" parent="1" vertex="1">
      <mxGeometry x="945" y="595" width="40" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-36" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="1" source="7a84cebc1def654-1" target="7a84cebc1def654-2" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-37" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;endArrow=none;endFill=0;" parent="1" source="7a84cebc1def654-4" target="7a84cebc1def654-2" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-38" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;endArrow=none;endFill=0;" parent="1" source="7a84cebc1def654-5" target="7a84cebc1def654-3" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-39" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="1" source="7a84cebc1def654-2" target="7a84cebc1def654-3" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-40" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="1" source="7a84cebc1def654-14" target="7a84cebc1def654-12" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-41" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;endArrow=none;endFill=0;" parent="1" source="7a84cebc1def654-27" target="7a84cebc1def654-14" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-42" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;endArrow=none;endFill=0;" parent="1" source="7a84cebc1def654-28" target="7a84cebc1def654-12" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-43" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="1" source="7a84cebc1def654-12" target="7a84cebc1def654-24" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="1289.9999999999995" y="475" as="targetPoint"/>
        <Array as="points">
          <mxPoint x="1280" y="290"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="7a84cebc1def654-44" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="1" source="7a84cebc1def654-16" target="7a84cebc1def654-24" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-45" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="1" source="7a84cebc1def654-18" target="7a84cebc1def654-24" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-46" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="1" source="7a84cebc1def654-24" target="7a84cebc1def654-26" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-47" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="1" source="7a84cebc1def654-3" target="7a84cebc1def654-6" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-48" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="1" source="7a84cebc1def654-6" target="7a84cebc1def654-8" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-49" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="1" source="7a84cebc1def654-8" target="7a84cebc1def654-9" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-50" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="1" source="7a84cebc1def654-9" target="7a84cebc1def654-14" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="720" y="290"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="7a84cebc1def654-51" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="1" source="7a84cebc1def654-9" target="7a84cebc1def654-29" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-52" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;endArrow=none;endFill=0;" parent="1" source="7a84cebc1def654-31" target="7a84cebc1def654-29" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-53" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=rhombusPerimeter;background=gateway;outline=none;symbol=parallelGw;" parent="1" vertex="1">
      <mxGeometry x="830" y="670" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-54" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="1" source="7a84cebc1def654-53" target="7a84cebc1def654-22" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="855" y="815"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="7a84cebc1def654-55" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="1" source="7a84cebc1def654-53" target="7a84cebc1def654-16" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="855" y="515"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="7a84cebc1def654-56" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;endArrow=none;endFill=0;" parent="1" source="7a84cebc1def654-35" target="7a84cebc1def654-16" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-58" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="1" source="7a84cebc1def654-29" target="7a84cebc1def654-53" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-59" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="1" source="7a84cebc1def654-22" target="7a84cebc1def654-20" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-60" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;endArrow=none;endFill=0;" parent="1" source="7a84cebc1def654-34" target="7a84cebc1def654-22" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-61" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;endArrow=none;endFill=0;" parent="1" source="7a84cebc1def654-32" target="7a84cebc1def654-20" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-63" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;endArrow=none;endFill=0;" parent="1" source="7a84cebc1def654-33" target="7a84cebc1def654-18" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="7a84cebc1def654-64" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;" parent="1" source="7a84cebc1def654-20" target="7a84cebc1def654-18" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>

```
