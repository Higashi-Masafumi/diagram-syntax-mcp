---
title: "Bpmn 2 Orgchart"
description: "An organizational chart showing hierarchy and reporting structure"
category: "examples"
type: "orgchart"
source_file: "examples/BPMN_2_decoded.xml"
tags: ["bpmn", "business_process", "sample", "drawio", "example"]
---

# Bpmn 2 Orgchart

An organizational chart showing hierarchy and reporting structure

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1122" dy="1074" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="0" page="0" pageScale="1" pageWidth="826" pageHeight="1169" background="#ffffff" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="2" value="&lt;span style=&quot;font-size: 14px;&quot;&gt;AGILE ORGANIZATION&lt;/span&gt;" style="rounded=0;whiteSpace=wrap;html=1;shadow=0;fillColor=#2F5B7C;fontFamily=Helvetica;fontSize=14;fontColor=#FFFFFF;align=center;verticalAlign=top;fontStyle=0;spacing=10;strokeColor=none;spacingTop=0;opacity=90;" parent="1" vertex="1">
      <mxGeometry x="182" y="-70" width="970" height="68" as="geometry"/>
    </mxCell>
    <mxCell id="3" value="Customer" style="swimlane;whiteSpace=wrap;fillColor=#F08705;swimlaneFillColor=#FCE7CD;fontColor=#FFFFFF;fontFamily=Helvetica;html=1;startSize=37;strokeColor=none;collapsible=0;fontSize=14;fontStyle=0;opacity=80;" parent="1" vertex="1">
      <mxGeometry x="20" width="160" height="780" as="geometry">
        <mxRectangle x="20" y="20" width="80" height="23" as="alternateBounds"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="4" value="Feature request or bug report" style="whiteSpace=wrap;strokeColor=none;fillColor=#F08705;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;fontSize=12;strokeWidth=2;opacity=80;" parent="3" vertex="1">
      <mxGeometry x="20" y="70" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="5" value="Feedback" style="rounded=0;whiteSpace=wrap;html=1;shadow=0;fillColor=#F08705;fontFamily=Helvetica;fontSize=12;fontColor=#FFFFFF;align=center;fontStyle=0;strokeColor=none;strokeWidth=2;opacity=80;" parent="3" vertex="1">
      <mxGeometry x="20" y="270" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="6" value="Feedback" style="rounded=0;whiteSpace=wrap;html=1;shadow=0;fillColor=#F08705;fontFamily=Helvetica;fontSize=12;fontColor=#FFFFFF;align=center;fontStyle=0;strokeColor=none;strokeWidth=2;opacity=80;" parent="3" vertex="1">
      <mxGeometry x="20" y="650" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="7" value="Translators" style="swimlane;whiteSpace=wrap;fillColor=#1699D3;swimlaneFillColor=#D0EBF6;fontColor=#FFFFFF;fontFamily=Helvetica;html=1;startSize=37;strokeColor=none;fontSize=14;fontStyle=0;opacity=80;" parent="1" vertex="1">
      <mxGeometry x="830" width="160" height="780" as="geometry">
        <mxRectangle x="20" y="20" width="80" height="23" as="alternateBounds"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="8" style="edgeStyle=orthogonalEdgeStyle;rounded=1;jumpStyle=gap;html=1;exitX=0.25;exitY=1;entryX=0.25;entryY=0;shadow=0;startArrow=none;startFill=0;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeWidth=2;fontFamily=Helvetica;fontSize=11;fontColor=#000000;fillColor=#f8cecc;strokeColor=#1699D3;startSize=3;endSize=3;" parent="7" source="9" target="10" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="9" value="UI &amp;amp;&lt;br&gt;documentation" style="whiteSpace=wrap;strokeColor=none;fillColor=#1699d3;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;opacity=80;" parent="7" vertex="1">
      <mxGeometry x="20" y="450" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="10" value="Marketing&lt;br&gt;materials" style="whiteSpace=wrap;strokeColor=none;fillColor=#1699d3;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;opacity=80;" parent="7" vertex="1">
      <mxGeometry x="20" y="564" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="11" value="QA" style="swimlane;whiteSpace=wrap;fillColor=#94CE41;swimlaneFillColor=#EAF5D9;fontColor=#FFFFFF;fontFamily=Helvetica;html=1;startSize=37;strokeColor=none;fontSize=14;fontStyle=0;opacity=80;" parent="1" vertex="1">
      <mxGeometry x="668" width="160" height="780" as="geometry">
        <mxRectangle x="20" y="20" width="80" height="23" as="alternateBounds"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="12" value="Testing" style="rhombus;whiteSpace=wrap;html=1;shadow=0;fillColor=#94CE41;fontFamily=Helvetica;fontSize=12;fontColor=#FFFFFF;align=center;strokeColor=none;fontStyle=0;spacing=0;verticalAlign=middle;opacity=80;" parent="11" vertex="1">
      <mxGeometry x="20" y="370" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="13" value="Product Owners" style="swimlane;whiteSpace=wrap;fillColor=#E85642;swimlaneFillColor=#FADDD9;fontColor=#FFFFFF;fontFamily=Helvetica;html=1;startSize=37;strokeColor=none;fontSize=14;fontStyle=0;opacity=80;" parent="1" vertex="1">
      <mxGeometry x="182" width="160" height="780" as="geometry">
        <mxRectangle x="180" y="20" width="80" height="23" as="alternateBounds"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="14" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;exitX=0.5;exitY=1;jettySize=auto;orthogonalLoop=1;fontFamily=Helvetica;fontSize=12;fontColor=#000000;fillColor=#e1d5e7;strokeColor=#E85642;strokeWidth=2;startSize=3;endSize=3;entryX=0.5;entryY=0;" parent="13" source="15" target="16" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="80" y="150" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="15" value="Goals, &lt;br style=&quot;font-size: 12px;&quot;&gt;requirements &amp;amp; planning" style="rhombus;whiteSpace=wrap;html=1;shadow=0;fontFamily=Helvetica;fontSize=12;fontColor=#FFFFFF;align=center;strokeColor=none;fillColor=#e85642;fontStyle=0;opacity=90;" parent="13" vertex="1">
      <mxGeometry x="20" y="60" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="16" value="&lt;font style=&quot;font-size: 12px&quot;&gt;&lt;span style=&quot;font-size: 12px&quot;&gt;Jira issues &amp;amp;&lt;br style=&quot;font-size: 12px;&quot;&gt;Confluence project documentation&lt;br style=&quot;font-size: 12px;&quot;&gt;&lt;/span&gt;&lt;/font&gt;" style="shape=document;whiteSpace=wrap;html=1;boundedLbl=1;fillColor=#e85642;fontSize=12;fontColor=#FFFFFF;align=center;fontFamily=Helvetica;fontStyle=0;shadow=0;strokeColor=none;spacingTop=6;opacity=90;" parent="13" vertex="1">
      <mxGeometry x="20" y="160" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="17" value="Meets&lt;br&gt;requirements?" style="rhombus;whiteSpace=wrap;html=1;shadow=0;fillColor=#e85642;fontFamily=Helvetica;fontSize=12;fontColor=#FFFFFF;align=center;strokeColor=none;fontStyle=0;spacingBottom=6;opacity=90;" parent="13" vertex="1">
      <mxGeometry x="20" y="260" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="18" value="Meets&lt;br&gt;requirements?" style="rhombus;whiteSpace=wrap;html=1;shadow=0;fillColor=#e85642;fontFamily=Helvetica;fontSize=12;fontColor=#FFFFFF;align=center;strokeColor=none;fontStyle=0;spacingBottom=6;opacity=90;" parent="13" vertex="1">
      <mxGeometry x="20" y="470" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="19" value="Meets goals?" style="rhombus;whiteSpace=wrap;html=1;shadow=0;fillColor=#e85642;fontFamily=Helvetica;fontSize=12;fontColor=#FFFFFF;align=center;strokeColor=none;fontStyle=0;opacity=90;" parent="13" vertex="1">
      <mxGeometry x="20" y="570" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="20" value="Programmers" style="swimlane;whiteSpace=wrap;fillColor=#94CE41;swimlaneFillColor=#EAF5D9;fontColor=#FFFFFF;fontFamily=Helvetica;html=1;startSize=37;strokeColor=none;fontSize=14;fontStyle=0;opacity=80;" parent="1" vertex="1">
      <mxGeometry x="344" width="160" height="780" as="geometry">
        <mxRectangle x="20" y="20" width="80" height="23" as="alternateBounds"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="21" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;jettySize=auto;orthogonalLoop=1;fontFamily=Helvetica;fontSize=12;fontColor=#000000;fillColor=#fff2cc;strokeColor=#94CE41;strokeWidth=2;startSize=3;endSize=3;" parent="20" source="22" target="24" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="22" value="Sprint planning" style="rhombus;whiteSpace=wrap;html=1;shadow=0;fillColor=#94CE41;fontFamily=Helvetica;fontSize=12;fontColor=#FFFFFF;align=center;strokeColor=none;fontStyle=0;spacing=0;verticalAlign=middle;gradientColor=none;opacity=80;" parent="20" vertex="1">
      <mxGeometry x="20" y="60" width="120" height="80" as="geometry"/>
    </mxCell>
    <mxCell id="23" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;jettySize=auto;orthogonalLoop=1;fontFamily=Helvetica;fontSize=12;fontColor=#000000;fillColor=#fff2cc;strokeColor=#C3CD2D;strokeWidth=2;startSize=3;endSize=3;" parent="20" source="24" target="26" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="24" value="Prototype(s)" style="whiteSpace=wrap;strokeColor=none;fillColor=#94CE41;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;opacity=80;" parent="20" vertex="1">
      <mxGeometry x="20" y="270" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="25" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;jettySize=auto;orthogonalLoop=1;fontFamily=Helvetica;fontSize=12;fontColor=#000000;fillColor=#fff2cc;strokeColor=#94CE41;strokeWidth=2;startSize=3;endSize=3;" parent="20" source="26" target="28" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="26" value="Implemention" style="whiteSpace=wrap;strokeColor=none;fillColor=#94CE41;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;opacity=80;" parent="20" vertex="1">
      <mxGeometry x="20" y="380" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="27" style="edgeStyle=orthogonalEdgeStyle;rounded=1;jumpStyle=gap;html=1;exitX=0.5;exitY=1;jettySize=auto;orthogonalLoop=1;fontFamily=Helvetica;fontSize=12;fontColor=#000000;fillColor=#fff2cc;strokeColor=#94CE41;strokeWidth=2;startSize=3;endSize=3;" parent="20" source="28" target="29" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="28" value="Release&lt;br&gt;candidate(s)" style="whiteSpace=wrap;strokeColor=none;fillColor=#94CE41;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;opacity=80;" parent="20" vertex="1">
      <mxGeometry x="20" y="480" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="29" value="&lt;font style=&quot;font-size: 12px&quot;&gt;&lt;span style=&quot;font-size: 12px&quot;&gt;Release&lt;/span&gt;&lt;/font&gt;" style="shape=document;whiteSpace=wrap;html=1;boundedLbl=1;fillColor=#94CE41;fontSize=12;fontColor=#FFFFFF;align=center;fontFamily=Helvetica;fontStyle=0;shadow=0;strokeColor=none;opacity=80;spacingTop=6;" parent="20" vertex="1">
      <mxGeometry x="20" y="650" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="30" value="Documentors" style="swimlane;whiteSpace=wrap;fillColor=#94CE41;swimlaneFillColor=#EAF5D9;fontColor=#FFFFFF;fontFamily=Helvetica;html=1;startSize=37;strokeColor=none;fontSize=14;fontStyle=0;opacity=80;" parent="1" vertex="1">
      <mxGeometry x="506" width="160" height="780" as="geometry">
        <mxRectangle x="20" y="20" width="80" height="23" as="alternateBounds"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="31" value="Documentation" style="whiteSpace=wrap;strokeColor=none;fillColor=#94CE41;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;opacity=80;" parent="30" vertex="1">
      <mxGeometry x="20" y="380" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="32" value="Requirements &amp;amp; design&lt;br&gt;documentation" style="whiteSpace=wrap;strokeColor=none;fillColor=#94CE41;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;opacity=80;" parent="30" vertex="1">
      <mxGeometry x="20" y="160" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="33" value="Marketing" style="swimlane;whiteSpace=wrap;fillColor=#736CA8;swimlaneFillColor=#E3E2EE;fontColor=#FFFFFF;fontFamily=Helvetica;html=1;startSize=37;strokeColor=none;fontSize=14;fontStyle=0;opacity=80;" parent="1" vertex="1">
      <mxGeometry x="992" width="160" height="780" as="geometry">
        <mxRectangle x="20" y="20" width="80" height="23" as="alternateBounds"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="34" style="edgeStyle=orthogonalEdgeStyle;rounded=1;jumpStyle=gap;html=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;jettySize=auto;orthogonalLoop=1;fontFamily=Helvetica;fontSize=12;fontColor=#000000;fillColor=#d5e8d4;strokeColor=#736CA8;strokeWidth=2;startSize=3;endSize=3;" parent="33" source="35" target="36" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="35" value="Marketing&lt;br&gt;materials" style="whiteSpace=wrap;strokeColor=none;fillColor=#736ca8;shadow=0;fontColor=#FFFFFF;fontFamily=Helvetica;fontStyle=0;html=1;opacity=80;" parent="33" vertex="1">
      <mxGeometry x="20" y="510" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="36" value="&lt;font style=&quot;font-size: 12px&quot;&gt;&lt;span style=&quot;font-size: 12px&quot;&gt;Marketing&lt;/span&gt;&lt;/font&gt;" style="shape=document;whiteSpace=wrap;html=1;boundedLbl=1;fillColor=#736ca8;fontSize=12;fontColor=#FFFFFF;align=center;fontFamily=Helvetica;fontStyle=0;shadow=0;strokeColor=none;opacity=80;spacingTop=6;" parent="33" vertex="1">
      <mxGeometry x="20" y="650" width="120" height="60" as="geometry"/>
    </mxCell>
    <mxCell id="37" value="INDIVIDUAL AGILE TEAMS" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#94CE41;fontSize=14;fontColor=#FFFFFF;align=center;fontStyle=0;fontFamily=Helvetica;strokeColor=none;opacity=50;" parent="1" vertex="1">
      <mxGeometry x="344" y="-30" width="484" height="28" as="geometry"/>
    </mxCell>
    <mxCell id="38" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;exitX=1;exitY=0.5;jettySize=auto;orthogonalLoop=1;fontFamily=Helvetica;fontSize=12;fontColor=#000000;fillColor=#ffe6cc;strokeColor=#F08705;strokeWidth=2;startSize=3;endSize=3;" parent="1" source="4" target="15" edge="1">
      <mxGeometry relative="1" as="geometry">
        <mxPoint x="200" y="130" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
    <mxCell id="39" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;jettySize=auto;orthogonalLoop=1;fontFamily=Helvetica;fontSize=12;fontColor=#000000;fillColor=#e1d5e7;strokeColor=#E85642;startArrow=classic;startFill=1;dashed=1;strokeWidth=2;startSize=3;endSize=3;" parent="1" source="15" target="22" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="40" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;jettySize=auto;orthogonalLoop=1;fontFamily=Helvetica;fontSize=12;fontColor=#000000;dashed=1;fillColor=#e1d5e7;strokeColor=#E85642;strokeWidth=2;startSize=3;endSize=3;" parent="1" source="17" target="24" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="41" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0.75;exitY=1;entryX=0.25;entryY=1;jettySize=auto;orthogonalLoop=1;fontFamily=Helvetica;fontSize=12;fontColor=#000000;fillColor=#ffe6cc;strokeColor=#F08705;strokeWidth=2;startSize=3;endSize=3;" parent="1" source="5" target="24" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="42" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0.25;exitY=0;entryX=0.75;entryY=0;jettySize=auto;orthogonalLoop=1;fontFamily=Helvetica;fontSize=12;fontColor=#000000;fillColor=#fff2cc;strokeColor=#94CE41;strokeWidth=2;startSize=3;endSize=3;" parent="1" source="24" target="5" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="43" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;jettySize=auto;orthogonalLoop=1;fontFamily=Helvetica;fontSize=12;fontColor=#000000;dashed=1;fillColor=#e1d5e7;strokeColor=#E85642;strokeWidth=2;startSize=3;endSize=3;" parent="1" source="18" target="28" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="44" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=1;exitY=0.5;entryX=0;entryY=0.5;jettySize=auto;orthogonalLoop=1;fontFamily=Helvetica;fontSize=12;fontColor=#000000;fillColor=#fff2cc;strokeColor=#94CE41;startArrow=classic;startFill=1;strokeWidth=2;startSize=3;endSize=3;" parent="1" source="26" target="31" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="45" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0.75;exitY=1;jettySize=auto;orthogonalLoop=1;fontFamily=Helvetica;fontSize=12;fontColor=#000000;fillColor=#fff2cc;strokeColor=#94CE41;entryX=0;entryY=0.25;jumpStyle=gap;strokeWidth=2;startSize=3;endSize=3;" parent="1" source="28" target="35" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="454" y="560"/>
          <mxPoint x="780" y="560"/>
          <mxPoint x="780" y="525"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="46" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0.864;exitY=-0.024;entryX=0.5;entryY=0;jettySize=auto;orthogonalLoop=1;fontFamily=Helvetica;fontSize=12;fontColor=#000000;fillColor=#fff2cc;strokeColor=#94CE41;startArrow=none;startFill=0;dashed=1;strokeWidth=2;exitPerimeter=0;startSize=3;endSize=3;" parent="1" source="26" target="12" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="468" y="340"/>
          <mxPoint x="748" y="340"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="47" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0.75;exitY=1;entryX=0;entryY=0.25;jettySize=auto;orthogonalLoop=1;fontFamily=Helvetica;fontSize=12;fontColor=#000000;jumpStyle=gap;fillColor=#fff2cc;strokeColor=#94CE41;strokeWidth=2;startSize=3;endSize=3;" parent="1" source="31" target="9" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="48" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;exitX=0;exitY=0.75;entryX=1;entryY=0.75;jettySize=auto;orthogonalLoop=1;fontFamily=Helvetica;fontSize=12;fontColor=#000000;fillColor=#f8cecc;strokeColor=#1699D3;strokeWidth=2;startSize=3;endSize=3;" parent="1" source="9" target="28" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="760" y="495"/>
          <mxPoint x="760" y="525"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="49" style="edgeStyle=orthogonalEdgeStyle;rounded=1;jumpStyle=gap;html=1;exitX=0;exitY=0.5;jettySize=auto;orthogonalLoop=1;fontFamily=Helvetica;fontSize=12;fontColor=#000000;endArrow=diamond;endFill=1;shadow=0;strokeWidth=2;fillColor=#dae8fc;strokeColor=#2F5B7C;startArrow=diamond;startFill=1;startSize=5;endSize=5;opacity=90;" parent="1" source="36" target="29" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="50" style="edgeStyle=orthogonalEdgeStyle;rounded=1;jumpStyle=gap;html=1;exitX=0.5;exitY=1;entryX=0.75;entryY=0;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;fontFamily=Helvetica;fontSize=12;fontColor=#000000;fillColor=#fff2cc;strokeColor=#94CE41;strokeWidth=2;startSize=3;endSize=3;" parent="1" source="31" target="28" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="51" style="edgeStyle=orthogonalEdgeStyle;rounded=1;jumpStyle=gap;html=1;exitX=0.5;exitY=1;entryX=1;entryY=0.25;shadow=0;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeWidth=2;fontFamily=Helvetica;fontSize=12;fontColor=#000000;fillColor=#fff2cc;strokeColor=#94CE41;startArrow=none;startFill=0;startSize=3;endSize=3;" parent="1" source="12" target="28" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="52" value="RETROSPECTIVE &amp;amp; REVIEW" style="rounded=0;whiteSpace=wrap;html=1;shadow=0;fillColor=#2f5b7c;fontFamily=Helvetica;fontSize=12;fontColor=#FFFFFF;align=center;strokeColor=none;fontStyle=0;opacity=90;" parent="1" vertex="1">
      <mxGeometry x="200" y="740" width="930" height="30" as="geometry"/>
    </mxCell>
    <mxCell id="53" style="edgeStyle=orthogonalEdgeStyle;rounded=1;jumpStyle=gap;html=1;exitX=0;exitY=0.5;entryX=1;entryY=0.5;shadow=0;startArrow=none;startFill=0;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeWidth=2;fontFamily=Helvetica;fontSize=11;fontColor=#000000;fillColor=#fff2cc;strokeColor=#94CE41;startSize=3;endSize=3;" parent="1" source="29" target="6" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="54" style="edgeStyle=orthogonalEdgeStyle;rounded=1;jumpStyle=gap;html=1;exitX=0.75;exitY=1;entryX=0;entryY=0.5;shadow=0;startArrow=none;startFill=0;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeWidth=2;fontFamily=Helvetica;fontSize=11;fontColor=#000000;fillColor=#ffe6cc;strokeColor=#F08705;startSize=3;endSize=3;" parent="1" source="6" target="52" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="55" style="edgeStyle=orthogonalEdgeStyle;rounded=1;jumpStyle=gap;html=1;exitX=0.25;exitY=1;entryX=1;entryY=0.5;shadow=0;startArrow=classic;startFill=1;endArrow=none;endFill=0;jettySize=auto;orthogonalLoop=1;strokeWidth=2;fontFamily=Helvetica;fontSize=11;fontColor=#000000;fillColor=#e1d5e7;strokeColor=#E85642;dashed=1;startSize=3;endSize=3;" parent="1" source="35" target="19" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="1042" y="640"/>
          <mxPoint x="640" y="640"/>
          <mxPoint x="640" y="610"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="56" style="edgeStyle=orthogonalEdgeStyle;rounded=1;jumpStyle=gap;html=1;exitX=0;exitY=0.5;entryX=0.5;entryY=0;shadow=0;startArrow=none;startFill=0;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeWidth=2;fontFamily=Helvetica;fontSize=11;fontColor=#000000;fillColor=#d5e8d4;strokeColor=#736CA8;startSize=3;endSize=3;" parent="1" source="35" target="10" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="57" style="edgeStyle=orthogonalEdgeStyle;rounded=1;jumpStyle=gap;html=1;exitX=1;exitY=0.5;entryX=0;entryY=0.75;shadow=0;startArrow=none;startFill=0;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeWidth=2;fontFamily=Helvetica;fontSize=11;fontColor=#000000;fillColor=#f8cecc;strokeColor=#1699D3;startSize=3;endSize=3;" parent="1" source="10" target="35" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="980" y="594"/>
          <mxPoint x="980" y="555"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="58" style="edgeStyle=orthogonalEdgeStyle;rounded=1;jumpStyle=gap;html=1;exitX=0;exitY=0.5;shadow=0;dashed=1;startArrow=none;startFill=0;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeWidth=2;fontFamily=Helvetica;fontSize=11;fontColor=#000000;fillColor=#fff2cc;strokeColor=#94CE41;startSize=3;endSize=3;" parent="1" source="12" target="26" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="660" y="410"/>
          <mxPoint x="660" y="360"/>
          <mxPoint x="450" y="360"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="59" style="edgeStyle=orthogonalEdgeStyle;rounded=1;jumpStyle=gap;html=1;exitX=0;exitY=0.5;entryX=1;entryY=0.375;entryPerimeter=0;shadow=0;startArrow=none;startFill=0;endArrow=classic;endFill=1;jettySize=auto;orthogonalLoop=1;strokeWidth=2;fontFamily=Helvetica;fontSize=11;fontColor=#000000;fillColor=#fff2cc;strokeColor=#94CE41;startSize=3;endSize=3;" parent="1" source="32" target="16" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
  </root>
</mxGraphModel>

```
