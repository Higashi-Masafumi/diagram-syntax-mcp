---
title: "Bpmn 1 Sequence"
description: "A sequence diagram illustrating interactions between objects over time"
category: "templates/business"
type: "sequence"
source_file: "templates/business/bpmn_1_decoded.xml"
tags: ["process", "bpmn", "template", "business", "business_process", "drawio", "workflow"]
---

# Bpmn 1 Sequence

A sequence diagram illustrating interactions between objects over time

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="239" dy="544" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1169" pageHeight="827" background="none" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="4022" value="" style="rounded=1;fillColor=#bac8d3;strokeWidth=3;html=1;strokeColor=none;arcSize=6;opacity=25;" parent="1" vertex="1">
      <mxGeometry x="1800" y="399.50000000000006" width="1660" height="301.49999999999994" as="geometry"/>
    </mxCell>
    <mxCell id="4023" value="" style="rounded=1;fillColor=#fad9d5;strokeWidth=2;html=1;strokeColor=none;arcSize=6;opacity=50;" parent="1" vertex="1">
      <mxGeometry x="2060" y="431" width="1220" height="230" as="geometry"/>
    </mxCell>
    <mxCell id="4024" value="" style="rounded=1;fillColor=#bac8d3;strokeWidth=3;html=1;strokeColor=none;arcSize=6;opacity=25;" parent="1" vertex="1">
      <mxGeometry x="1800" y="21" width="1660" height="180" as="geometry"/>
    </mxCell>
    <mxCell id="4025" value="" style="edgeStyle=none;endArrow=none;startArrow=none;strokeWidth=3;html=1;strokeColor=#FFFFFF;" parent="1" edge="1">
      <mxGeometry x="1892.5" y="-79.75" width="100" height="100" as="geometry">
        <mxPoint x="1870" y="20.249999999999773" as="sourcePoint"/>
        <mxPoint x="1870" y="200.25" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4026" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=ellipsePerimeter;outline=standard;symbol=message;fontFamily=Helvetica;fontSize=12;fontColor=#000000;align=center;strokeColor=#F08705;strokeWidth=3;fillColor=none;" parent="1" vertex="1">
      <mxGeometry x="1930" y="78.5" width="65" height="65" as="geometry"/>
    </mxCell>
    <mxCell id="4027" value="Get Task" style="rounded=1;fillColor=#f08705;strokeWidth=2;html=1;strokeColor=none;fontColor=#FFFFFF;fontSize=16;" parent="1" vertex="1">
      <mxGeometry x="2100" y="79.5" width="160" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="4028" value="Create Schedule" style="rounded=1;fillColor=#f08705;strokeWidth=2;html=1;strokeColor=none;fontColor=#FFFFFF;fontSize=16;" parent="1" vertex="1">
      <mxGeometry x="2370" y="79.5" width="210" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="4029" value="Verify Schedule" style="rounded=1;fillColor=#f08705;strokeWidth=2;html=1;strokeColor=none;fontColor=#FFFFFF;fontSize=16;" parent="1" vertex="1">
      <mxGeometry x="2690" y="80.9" width="210" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="4030" value="Commit Schedule" style="rounded=1;fillColor=#f08705;strokeWidth=2;html=1;strokeColor=none;fontColor=#FFFFFF;fontSize=16;" parent="1" vertex="1">
      <mxGeometry x="2990" y="81" width="200" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="4031" value="" style="edgeStyle=none;exitX=1;exitY=0.5;exitPerimeter=0;strokeWidth=3;html=1;strokeColor=#F08705;" parent="1" source="4026" target="4027" edge="1">
      <mxGeometry x="1780" y="1" width="100" height="100" as="geometry">
        <mxPoint x="1780" y="101" as="sourcePoint"/>
        <mxPoint x="1880" y="1" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4032" value="" style="edgeStyle=none;strokeWidth=3;html=1;strokeColor=#F08705;" parent="1" source="4027" target="4028" edge="1">
      <mxGeometry x="1780" y="1" width="100" height="100" as="geometry">
        <mxPoint x="1780" y="101" as="sourcePoint"/>
        <mxPoint x="1880" y="1" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4033" value="" style="edgeStyle=none;strokeWidth=3;html=1;strokeColor=#F08705;" parent="1" source="4028" target="4029" edge="1">
      <mxGeometry x="1780" y="1" width="100" height="100" as="geometry">
        <mxPoint x="1780" y="101" as="sourcePoint"/>
        <mxPoint x="1880" y="1" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4034" value="" style="edgeStyle=none;strokeWidth=3;html=1;strokeColor=#F08705;" parent="1" source="4029" target="4030" edge="1">
      <mxGeometry x="1780" y="1" width="100" height="100" as="geometry">
        <mxPoint x="1780" y="101" as="sourcePoint"/>
        <mxPoint x="1880" y="1" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4035" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=ellipsePerimeter;outline=end;symbol=general;fontFamily=Helvetica;fontSize=12;fontColor=#000000;align=center;strokeColor=#f08705;strokeWidth=3;fillColor=none;" parent="1" vertex="1">
      <mxGeometry x="3330" y="78.50000000000001" width="65" height="65" as="geometry"/>
    </mxCell>
    <mxCell id="4036" value="" style="edgeStyle=none;strokeWidth=3;html=1;strokeColor=#F08705;" parent="1" source="4030" target="4035" edge="1">
      <mxGeometry x="1780" y="1" width="100" height="100" as="geometry">
        <mxPoint x="1780" y="101" as="sourcePoint"/>
        <mxPoint x="1880" y="1" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4037" value="SCHEDULING" style="text;horizontal=0;fontSize=20;fontStyle=1;html=1;fontColor=#F08705;labelBackgroundColor=none;align=center;" parent="1" vertex="1">
      <mxGeometry x="1819" y="36" width="34" height="150" as="geometry"/>
    </mxCell>
    <mxCell id="4038" value="&lt;font style=&quot;font-size: 16px&quot;&gt;Order list&lt;/font&gt;" style="shape=note;verticalLabelPosition=middle;verticalAlign=middle;strokeWidth=3;html=1;spacingLeft=5;align=left;strokeColor=#2f5b7c;fontColor=#2F5B7C;spacingRight=4;spacingTop=30;labelPosition=right;fillColor=none;" parent="1" vertex="1">
      <mxGeometry x="2120" y="241" width="60" height="90" as="geometry"/>
    </mxCell>
    <mxCell id="4039" value="" style="edgeStyle=none;endArrow=none;startArrow=none;strokeWidth=3;html=1;strokeColor=#FFFFFF;" parent="1" edge="1">
      <mxGeometry x="1895.25" y="299.50000000000006" width="100" height="100" as="geometry">
        <mxPoint x="1872.75" y="399.5" as="sourcePoint"/>
        <mxPoint x="1870.25" y="701" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4040" value="Compose Specification" style="rounded=1;fillColor=#e85642;strokeWidth=2;html=1;strokeColor=none;fontColor=#FFFFFF;fontSize=16;" parent="1" vertex="1">
      <mxGeometry x="2250" y="458" width="190" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="4041" value="Check warehouse" style="rounded=1;fillColor=#e85642;strokeWidth=2;html=1;strokeColor=none;fontColor=#FFFFFF;fontSize=16;" parent="1" vertex="1">
      <mxGeometry x="2520" y="458.75000000000006" width="150" height="59.99999999999994" as="geometry"/>
    </mxCell>
    <mxCell id="4042" value="Produce Goods" style="rounded=1;fillColor=#e85642;strokeWidth=2;html=1;strokeColor=none;fontColor=#FFFFFF;fontSize=16;" parent="1" vertex="1">
      <mxGeometry x="2890" y="458.5" width="200" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="4043" value="" style="edgeStyle=none;strokeWidth=3;html=1;strokeColor=#e85642;" parent="1" source="4040" target="4041" edge="1">
      <mxGeometry x="1790" y="379.50000000000006" width="100" height="100" as="geometry">
        <mxPoint x="1790" y="479.50000000000006" as="sourcePoint"/>
        <mxPoint x="1890" y="379.50000000000006" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4044" value="" style="edgeStyle=none;strokeWidth=3;html=1;strokeColor=#e85642;" parent="1" source="4042" target="4052" edge="1">
      <mxGeometry x="1790" y="379.50000000000006" width="100" height="100" as="geometry">
        <mxPoint x="1790" y="479.50000000000006" as="sourcePoint"/>
        <mxPoint x="1890" y="379.50000000000006" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4045" value="FACTORY" style="text;horizontal=0;fontSize=20;fontStyle=1;html=1;strokeColor=none;fontColor=#E85642;labelBackgroundColor=none;align=center;" parent="1" vertex="1">
      <mxGeometry x="1819" y="475.24999999999994" width="34" height="150" as="geometry"/>
    </mxCell>
    <mxCell id="4046" style="edgeStyle=none;html=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;startArrow=none;startFill=0;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeColor=#e85642;strokeWidth=3;fontSize=15;fontColor=#FFFFFF;" parent="1" source="4048" target="4042" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="4047" value="&lt;font style=&quot;font-size: 16px&quot; color=&quot;#e85642&quot;&gt;Yes&lt;/font&gt;" style="text;html=1;resizable=0;points=[];align=center;verticalAlign=middle;labelBackgroundColor=none;fontSize=15;fontColor=#FFFFFF;spacingBottom=29;" parent="4046" vertex="1" connectable="0">
      <mxGeometry x="-0.1708" y="-2" relative="1" as="geometry">
        <mxPoint as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4048" value="Available?" style="rounded=1;whiteSpace=wrap;html=1;fontFamily=Helvetica;fontSize=16;fontColor=#FFFFFF;align=center;strokeColor=none;strokeWidth=2;fillColor=#e85642;" parent="1" vertex="1">
      <mxGeometry x="2730" y="463" width="100" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="4049" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=ellipsePerimeter;outline=eventInt;symbol=message;fontFamily=Helvetica;fontSize=12;fontColor=#000000;align=center;strokeColor=#e85642;strokeWidth=3;fillColor=none;" parent="1" vertex="1">
      <mxGeometry x="2755" y="571" width="49.99999999999997" height="49.80000000000001" as="geometry"/>
    </mxCell>
    <mxCell id="4050" value="&lt;font style=&quot;font-size: 16px&quot; color=&quot;#e85642&quot;&gt;No&lt;/font&gt;" style="edgeStyle=orthogonalEdgeStyle;strokeWidth=3;html=1;labelBackgroundColor=none;align=left;strokeColor=#E85642;spacingRight=0;spacingTop=0;spacingBottom=7;spacingLeft=3;" parent="1" source="4048" target="4049" edge="1">
      <mxGeometry x="1780" y="1" width="100" height="100" as="geometry">
        <mxPoint x="1780" y="101" as="sourcePoint"/>
        <mxPoint x="1880" y="1" as="targetPoint"/>
        <mxPoint y="-4" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4051" value="" style="edgeStyle=orthogonalEdgeStyle;strokeWidth=3;html=1;strokeColor=#e85642;" parent="1" source="4049" target="4042" edge="1">
      <mxGeometry x="1780" y="1" width="100" height="100" as="geometry">
        <mxPoint x="1780" y="101" as="sourcePoint"/>
        <mxPoint x="1880" y="1" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4052" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=ellipsePerimeter;outline=end;symbol=message;fontFamily=Helvetica;fontSize=12;fontColor=#000000;align=center;strokeColor=#E85642;strokeWidth=2;fillColor=#FAD9D5;" parent="1" vertex="1">
      <mxGeometry x="3165" y="463.20000000000005" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="4053" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=ellipsePerimeter;outline=standard;symbol=general;fontFamily=Helvetica;fontSize=12;fontColor=#000000;align=center;strokeColor=#e85642;strokeWidth=3;fillColor=none;" parent="1" vertex="1">
      <mxGeometry x="2120" y="463.50000000000006" width="50" height="50" as="geometry"/>
    </mxCell>
    <mxCell id="4054" value="" style="edgeStyle=none;strokeWidth=3;html=1;strokeColor=#e85642;" parent="1" source="4053" target="4040" edge="1">
      <mxGeometry x="1780" y="1" width="100" height="100" as="geometry">
        <mxPoint x="1780" y="101" as="sourcePoint"/>
        <mxPoint x="1880" y="1" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4055" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=ellipsePerimeter;outline=eventInt;symbol=timer;fontFamily=Helvetica;fontSize=12;fontColor=#000000;align=center;strokeColor=#e85642;strokeWidth=3;fillColor=none;" parent="1" vertex="1">
      <mxGeometry x="1930" y="517.75" width="65" height="65" as="geometry"/>
    </mxCell>
    <mxCell id="4056" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;strokeWidth=3;html=1;strokeColor=#e85642;" parent="1" source="4055" edge="1">
      <mxGeometry x="1780" y="1" width="100" height="100" as="geometry">
        <mxPoint x="1780" y="101" as="sourcePoint"/>
        <mxPoint x="2060" y="550" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4057" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=ellipsePerimeter;outline=end;symbol=general;fontFamily=Helvetica;fontSize=12;fontColor=#000000;align=center;strokeColor=#e85642;strokeWidth=3;fillColor=none;" parent="1" vertex="1">
      <mxGeometry x="3330" y="517.75" width="65" height="65" as="geometry"/>
    </mxCell>
    <mxCell id="4058" value="" style="edgeStyle=elbowEdgeStyle;elbow=vertical;strokeWidth=3;html=1;strokeColor=#e85642;" parent="1" target="4057" edge="1">
      <mxGeometry x="1780" y="1" width="100" height="100" as="geometry">
        <mxPoint x="3280" y="550" as="sourcePoint"/>
        <mxPoint x="1880" y="1" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4059" value="&lt;font style=&quot;font-size: 16px&quot;&gt;Order Completed&lt;/font&gt;" style="edgeStyle=elbowEdgeStyle;elbow=vertical;dashed=1;rounded=1;strokeWidth=3;html=1;verticalAlign=bottom;strokeColor=#2f5b7c;fontSize=15;fontColor=#2F5B7C;spacingBottom=2;" parent="1" source="4052" target="4028" edge="1">
      <mxGeometry width="100" height="100" as="geometry">
        <mxPoint x="1780" y="101" as="sourcePoint"/>
        <mxPoint x="1880" y="1" as="targetPoint"/>
        <mxPoint x="-12" as="offset"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4060" value="" style="edgeStyle=none;dashed=1;strokeWidth=3;html=1;strokeColor=#2f5b7c;" parent="1" source="4028" target="4038" edge="1">
      <mxGeometry x="1780" y="1" width="100" height="100" as="geometry">
        <mxPoint x="1780" y="101" as="sourcePoint"/>
        <mxPoint x="1880" y="1" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4061" style="edgeStyle=none;html=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;startArrow=none;startFill=0;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeColor=#e85642;strokeWidth=3;fontSize=15;fontColor=#FFFFFF;" parent="1" source="4041" target="4048" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="4062" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;dashed=1;startArrow=classic;endArrow=classic;strokeWidth=3;html=1;strokeColor=#2f5b7c;" parent="1" source="4038" edge="1">
      <mxGeometry x="1730" y="1" width="100" height="100" as="geometry">
        <mxPoint x="1730" y="101" as="sourcePoint"/>
        <mxPoint x="2150" y="431" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4063" value="" style="rounded=1;fillColor=#bac8d3;strokeWidth=3;html=1;strokeColor=none;arcSize=6;opacity=25;" parent="1" vertex="1">
      <mxGeometry x="1800" y="921" width="1660" height="180" as="geometry"/>
    </mxCell>
    <mxCell id="4064" value="" style="edgeStyle=none;endArrow=none;startArrow=none;strokeWidth=3;html=1;strokeColor=#FFFFFF;fontColor=#0E8088;" parent="1" edge="1">
      <mxGeometry x="1898.07" y="821" width="100" height="100" as="geometry">
        <mxPoint x="1870" y="921" as="sourcePoint"/>
        <mxPoint x="1870" y="1101" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4065" value="&lt;div style=&quot;text-align: center&quot;&gt;&lt;span&gt;ANALYSIS&lt;/span&gt;&lt;/div&gt;" style="text;horizontal=0;fontSize=20;fontStyle=1;html=1;fontColor=#12AAB5;labelBackgroundColor=none;align=center;" parent="1" vertex="1">
      <mxGeometry x="1819" y="936" width="34" height="150" as="geometry"/>
    </mxCell>
    <mxCell id="4066" value="Quality Control" style="rounded=1;fillColor=#12aab5;strokeWidth=2;html=1;strokeColor=none;fontColor=#FFFFFF;fontSize=16;" parent="1" vertex="1">
      <mxGeometry x="2210" y="981" width="160" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="4067" value="Issue Revision" style="rounded=1;fillColor=#12aab5;strokeWidth=2;html=1;strokeColor=none;fontColor=#FFFFFF;fontSize=16;" parent="1" vertex="1">
      <mxGeometry x="2505" y="981" width="160" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="4068" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=ellipsePerimeter;outline=eventInt;symbol=timer;fontFamily=Helvetica;fontSize=12;fontColor=#000000;align=center;strokeColor=#12AAB5;strokeWidth=3;fillColor=none;" parent="1" vertex="1">
      <mxGeometry x="1930" y="978.5" width="65" height="65" as="geometry"/>
    </mxCell>
    <mxCell id="4069" value="" style="shape=mxgraph.bpmn.shape;html=1;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;perimeter=ellipsePerimeter;outline=end;symbol=general;fontFamily=Helvetica;fontSize=12;fontColor=#000000;align=center;strokeColor=#12AAB5;strokeWidth=3;fillColor=none;" parent="1" vertex="1">
      <mxGeometry x="2810" y="978.5" width="65" height="65" as="geometry"/>
    </mxCell>
    <mxCell id="4070" value="" style="edgeStyle=none;dashed=1;strokeWidth=3;html=1;strokeColor=#2f5b7c;" parent="1" source="4041" target="4072" edge="1">
      <mxGeometry x="1900.8711048158639" y="612.5" width="100" height="100" as="geometry">
        <mxPoint x="2549.128895184136" y="751" as="sourcePoint"/>
        <mxPoint x="2350.871104815864" y="878.2454545454545" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4071" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;dashed=1;startArrow=classic;endArrow=classic;strokeWidth=3;html=1;strokeColor=#2f5b7c;" parent="1" source="4072" target="4066" edge="1">
      <mxGeometry x="1823.6" y="581" width="100" height="100" as="geometry">
        <mxPoint x="2243.6" y="911" as="sourcePoint"/>
        <mxPoint x="2243.6" y="1011" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4072" value="&lt;font style=&quot;font-size: 16px&quot; color=&quot;#23445d&quot;&gt;Planned&lt;br&gt; Stock Balance&lt;/font&gt;" style="shape=note;verticalLabelPosition=middle;verticalAlign=middle;strokeWidth=3;html=1;align=left;spacingLeft=5;strokeColor=#2f5b7c;labelPosition=right;spacingTop=20;fontColor=#2F5B7C;fillColor=none;" parent="1" vertex="1">
      <mxGeometry x="2230" y="761" width="60" height="90" as="geometry"/>
    </mxCell>
    <mxCell id="4073" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;strokeWidth=3;html=1;strokeColor=#12AAB5;" parent="1" source="4068" target="4066" edge="1">
      <mxGeometry x="1785" y="-64.00000000000023" width="100" height="100" as="geometry">
        <mxPoint x="1785" y="35.99999999999977" as="sourcePoint"/>
        <mxPoint x="1885" y="-64.00000000000023" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4074" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;strokeWidth=3;html=1;strokeColor=#12AAB5;" parent="1" source="4066" target="4067" edge="1">
      <mxGeometry x="1795" y="-64.00000000000023" width="100" height="100" as="geometry">
        <mxPoint x="1795" y="35.99999999999977" as="sourcePoint"/>
        <mxPoint x="1895" y="-64.00000000000023" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4075" value="" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;strokeWidth=3;html=1;strokeColor=#12AAB5;" parent="1" source="4067" target="4069" edge="1">
      <mxGeometry x="1795" y="-64.00000000000023" width="100" height="100" as="geometry">
        <mxPoint x="1795" y="35.99999999999977" as="sourcePoint"/>
        <mxPoint x="1895" y="-64.00000000000023" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4076" value="&lt;font style=&quot;font-size: 16px&quot; color=&quot;#2f5b7c&quot;&gt;Materials Delivered&lt;/font&gt;" style="edgeStyle=elbowEdgeStyle;elbow=vertical;dashed=1;strokeWidth=3;html=1;verticalAlign=bottom;strokeColor=#2f5b7c;fontSize=14;fontColor=#0E8088;spacingBottom=1;" parent="1" source="4067" target="4049" edge="1">
      <mxGeometry x="1780" y="1" width="100" height="100" as="geometry">
        <mxPoint x="1780" y="101" as="sourcePoint"/>
        <mxPoint x="1880" y="1" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4077" value="&amp;nbsp; &amp;nbsp;" style="text;html=1;resizable=0;points=[];autosize=1;align=left;verticalAlign=top;spacingTop=-4;fontSize=30;fontColor=#f08705;" parent="1" vertex="1">
      <mxGeometry x="2276" y="800" width="35" height="36" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>

```
