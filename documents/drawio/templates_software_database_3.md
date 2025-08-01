---
title: "Database 3 Database"
description: "A database diagram showing entity relationships and structure"
category: "templates/software"
type: "database"
source_file: "templates/software/database_3_decoded.xml"
tags: ["development", "software", "database", "template", "architecture", "erd", "drawio", "data"]
---

# Database 3 Database

A database diagram showing entity relationships and structure

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="1408" dy="544" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1100" pageHeight="850" background="none" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="2ed32ef02a7f4228-1" value="&lt;div style=&quot;box-sizing:border-box;width:100%;background:#e4e4e4;padding:2px;&quot;&gt;Tablename&lt;/div&gt;&lt;table style=&quot;width:100%;font-size:1em;&quot; cellpadding=&quot;2&quot; cellspacing=&quot;0&quot;&gt;&lt;tr&gt;&lt;td&gt;PK&lt;/td&gt;&lt;td&gt;uniqueId&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;/td&gt;&lt;td&gt;foreignKey&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;" style="verticalAlign=top;align=left;overflow=fill;html=1;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="110" y="100" width="180" height="90" as="geometry"/>
    </mxCell>
    <mxCell id="2ed32ef02a7f4228-18" style="edgeStyle=orthogonalEdgeStyle;html=1;entryX=0.5;entryY=0;dashed=1;labelBackgroundColor=none;startArrow=ERmandOne;endArrow=ERoneToMany;fontFamily=Verdana;fontSize=12;align=left;" parent="1" source="2ed32ef02a7f4228-2" target="2ed32ef02a7f4228-8" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ed32ef02a7f4228-19" style="edgeStyle=orthogonalEdgeStyle;html=1;dashed=1;labelBackgroundColor=none;startArrow=ERmandOne;endArrow=ERoneToMany;fontFamily=Verdana;fontSize=12;align=left;entryX=0;entryY=0.5;" parent="1" source="2ed32ef02a7f4228-2" target="2ed32ef02a7f4228-10" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="590" y="260"/>
          <mxPoint x="710" y="260"/>
          <mxPoint x="710" y="325"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="2ed32ef02a7f4228-20" style="edgeStyle=orthogonalEdgeStyle;html=1;dashed=1;labelBackgroundColor=none;startArrow=ERmandOne;endArrow=ERoneToMany;fontFamily=Verdana;fontSize=12;align=left;" parent="1" source="2ed32ef02a7f4228-2" target="2ed32ef02a7f4228-11" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ed32ef02a7f4228-2" value="&lt;div style=&quot;box-sizing: border-box ; width: 100% ; background: #e4e4e4 ; padding: 2px&quot;&gt;Tablename&lt;/div&gt;&lt;table style=&quot;width: 100% ; font-size: 1em&quot; cellpadding=&quot;2&quot; cellspacing=&quot;0&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;PK&lt;/td&gt;&lt;td&gt;uniqueId&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;/td&gt;&lt;td&gt;foreignKey&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;br&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;br&gt;&lt;/td&gt;&lt;td&gt;foreignKey&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;br&gt;&lt;/td&gt;&lt;td&gt;foreignKey&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;" style="verticalAlign=top;align=left;overflow=fill;html=1;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="460" y="100" width="180" height="130" as="geometry"/>
    </mxCell>
    <mxCell id="2ed32ef02a7f4228-16" style="edgeStyle=orthogonalEdgeStyle;html=1;labelBackgroundColor=none;startArrow=ERmandOne;endArrow=ERoneToMany;fontFamily=Verdana;fontSize=12;align=left;" parent="1" source="2ed32ef02a7f4228-3" target="2ed32ef02a7f4228-4" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ed32ef02a7f4228-22" style="edgeStyle=orthogonalEdgeStyle;html=1;exitX=0;exitY=0.75;entryX=1;entryY=0.5;dashed=1;labelBackgroundColor=none;startArrow=ERmandOne;endArrow=ERoneToMany;fontFamily=Verdana;fontSize=12;align=left;" parent="1" source="2ed32ef02a7f4228-8" target="2ed32ef02a7f4228-3" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ed32ef02a7f4228-3" value="&lt;div style=&quot;box-sizing: border-box ; width: 100% ; background: #e4e4e4 ; padding: 2px&quot;&gt;Tablename&lt;/div&gt;&lt;table style=&quot;width: 100% ; font-size: 1em&quot; cellpadding=&quot;2&quot; cellspacing=&quot;0&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;PK&lt;/td&gt;&lt;td&gt;uniqueId&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;/td&gt;&lt;td&gt;foreignKey&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;br&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;" style="verticalAlign=top;align=left;overflow=fill;html=1;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="110" y="540" width="180" height="90" as="geometry"/>
    </mxCell>
    <mxCell id="2ed32ef02a7f4228-4" value="&lt;div style=&quot;box-sizing: border-box ; width: 100% ; background: #e4e4e4 ; padding: 2px&quot;&gt;Tablename&lt;/div&gt;&lt;table style=&quot;width: 100% ; font-size: 1em&quot; cellpadding=&quot;2&quot; cellspacing=&quot;0&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;PK&lt;/td&gt;&lt;td&gt;uniqueId&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;/td&gt;&lt;td&gt;foreignKey&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;br&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;" style="verticalAlign=top;align=left;overflow=fill;html=1;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="110" y="410" width="180" height="90" as="geometry"/>
    </mxCell>
    <mxCell id="2ed32ef02a7f4228-15" style="edgeStyle=orthogonalEdgeStyle;html=1;entryX=0.5;entryY=0;labelBackgroundColor=none;startArrow=ERmandOne;endArrow=ERoneToMany;fontFamily=Verdana;fontSize=12;align=left;" parent="1" source="2ed32ef02a7f4228-5" target="2ed32ef02a7f4228-4" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ed32ef02a7f4228-5" value="&lt;div style=&quot;box-sizing:border-box;width:100%;background:#e4e4e4;padding:2px;&quot;&gt;Tablename&lt;/div&gt;&lt;table style=&quot;width:100%;font-size:1em;&quot; cellpadding=&quot;2&quot; cellspacing=&quot;0&quot;&gt;&lt;tr&gt;&lt;td&gt;PK&lt;/td&gt;&lt;td&gt;uniqueId&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;/td&gt;&lt;td&gt;foreignKey&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;" style="verticalAlign=top;align=left;overflow=fill;html=1;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="110" y="250" width="180" height="90" as="geometry"/>
    </mxCell>
    <mxCell id="2ed32ef02a7f4228-6" value="&lt;div style=&quot;box-sizing: border-box ; width: 100% ; background: #e4e4e4 ; padding: 2px&quot;&gt;Tablename&lt;/div&gt;&lt;table style=&quot;width: 100% ; font-size: 1em&quot; cellpadding=&quot;2&quot; cellspacing=&quot;0&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;PK&lt;/td&gt;&lt;td&gt;uniqueId&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;/td&gt;&lt;td&gt;foreignKey&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;br&gt;&lt;/td&gt;&lt;td&gt;foreignKey&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;br&gt;&lt;/td&gt;&lt;td&gt;foreignKey&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;br&gt;&lt;/td&gt;&lt;td&gt;foreignKey&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;br&gt;&lt;/td&gt;&lt;td&gt;foreignKey&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;br&gt;&lt;/td&gt;&lt;td&gt;foreignKey&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;br&gt;&lt;/td&gt;&lt;td&gt;foreignKey&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;br&gt;&lt;/td&gt;&lt;td&gt;foreignKey&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;" style="verticalAlign=top;align=left;overflow=fill;html=1;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="830" y="600" width="180" height="205" as="geometry"/>
    </mxCell>
    <mxCell id="2ed32ef02a7f4228-7" value="&lt;div style=&quot;box-sizing: border-box ; width: 100% ; background: #e4e4e4 ; padding: 2px&quot;&gt;Tablename&lt;/div&gt;&lt;table style=&quot;width: 100% ; font-size: 1em&quot; cellpadding=&quot;2&quot; cellspacing=&quot;0&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;PK&lt;/td&gt;&lt;td&gt;uniqueId&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;/td&gt;&lt;td&gt;foreignKey&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;br&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;br&gt;&lt;/td&gt;&lt;td&gt;foreignKey&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;" style="verticalAlign=top;align=left;overflow=fill;html=1;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="460" y="680" width="180" height="110" as="geometry"/>
    </mxCell>
    <mxCell id="2ed32ef02a7f4228-17" style="edgeStyle=orthogonalEdgeStyle;html=1;entryX=0.5;entryY=0;labelBackgroundColor=none;startArrow=ERmandOne;endArrow=ERoneToMany;fontFamily=Verdana;fontSize=12;align=left;dashed=1;" parent="1" source="2ed32ef02a7f4228-8" target="2ed32ef02a7f4228-7" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ed32ef02a7f4228-8" value="&lt;div style=&quot;box-sizing: border-box ; width: 100% ; background: #e4e4e4 ; padding: 2px&quot;&gt;Tablename&lt;/div&gt;&lt;table style=&quot;width: 100% ; font-size: 1em&quot; cellpadding=&quot;2&quot; cellspacing=&quot;0&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;PK&lt;/td&gt;&lt;td&gt;uniqueId&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;/td&gt;&lt;td&gt;foreignKey&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;br&gt;&lt;/td&gt;&lt;td&gt;foreignKey&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;br&gt;&lt;/td&gt;&lt;td&gt;foreignKey&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;br&gt;&lt;/td&gt;&lt;td&gt;foreignKey&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;br&gt;&lt;/td&gt;&lt;td&gt;foreignKey&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;br&gt;&lt;/td&gt;&lt;td&gt;foreignKey&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;br&gt;&lt;/td&gt;&lt;td&gt;foreignKey&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;br&gt;&lt;/td&gt;&lt;td&gt;foreignKey&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;br&gt;&lt;/td&gt;&lt;td&gt;foreignKey&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;br&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;br&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;br&gt;&lt;/td&gt;&lt;td&gt;foreignKey&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;br&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;br&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;br&gt;&lt;/td&gt;&lt;td&gt;foreignKey&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;" style="verticalAlign=top;align=left;overflow=fill;html=1;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="460" y="280" width="180" height="330" as="geometry"/>
    </mxCell>
    <mxCell id="2ed32ef02a7f4228-9" value="&lt;div style=&quot;box-sizing:border-box;width:100%;background:#e4e4e4;padding:2px;&quot;&gt;Tablename&lt;/div&gt;&lt;table style=&quot;width:100%;font-size:1em;&quot; cellpadding=&quot;2&quot; cellspacing=&quot;0&quot;&gt;&lt;tr&gt;&lt;td&gt;PK&lt;/td&gt;&lt;td&gt;uniqueId&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;/td&gt;&lt;td&gt;foreignKey&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;" style="verticalAlign=top;align=left;overflow=fill;html=1;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="830" y="490" width="180" height="90" as="geometry"/>
    </mxCell>
    <mxCell id="2ed32ef02a7f4228-21" style="edgeStyle=orthogonalEdgeStyle;html=1;entryX=0.5;entryY=0;dashed=1;labelBackgroundColor=none;startArrow=ERmandOne;endArrow=ERoneToMany;fontFamily=Verdana;fontSize=12;align=left;" parent="1" source="2ed32ef02a7f4228-10" target="2ed32ef02a7f4228-9" edge="1">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="2ed32ef02a7f4228-10" value="&lt;div style=&quot;box-sizing: border-box ; width: 100% ; background: #e4e4e4 ; padding: 2px&quot;&gt;Tablename&lt;/div&gt;&lt;table style=&quot;width: 100% ; font-size: 1em&quot; cellpadding=&quot;2&quot; cellspacing=&quot;0&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;PK&lt;/td&gt;&lt;td&gt;uniqueId&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;/td&gt;&lt;td&gt;foreignKey&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;br&gt;&lt;/td&gt;&lt;td&gt;foreignKey&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;br&gt;&lt;/td&gt;&lt;td&gt;foreignKey&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;br&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;br&gt;&lt;/td&gt;&lt;td&gt;foreignKey&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;br&gt;&lt;/td&gt;&lt;td&gt;foreignKey&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;br&gt;&lt;/td&gt;&lt;td&gt;foreignKey&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;br&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;br&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;br&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;" style="verticalAlign=top;align=left;overflow=fill;html=1;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="830" y="210" width="180" height="240" as="geometry"/>
    </mxCell>
    <mxCell id="2ed32ef02a7f4228-11" value="&lt;div style=&quot;box-sizing:border-box;width:100%;background:#e4e4e4;padding:2px;&quot;&gt;Tablename&lt;/div&gt;&lt;table style=&quot;width:100%;font-size:1em;&quot; cellpadding=&quot;2&quot; cellspacing=&quot;0&quot;&gt;&lt;tr&gt;&lt;td&gt;PK&lt;/td&gt;&lt;td&gt;uniqueId&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;/td&gt;&lt;td&gt;foreignKey&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;" style="verticalAlign=top;align=left;overflow=fill;html=1;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="830" y="90" width="180" height="90" as="geometry"/>
    </mxCell>
    <mxCell id="2ed32ef02a7f4228-12" value="&lt;div style=&quot;box-sizing: border-box ; width: 100% ; background: #e4e4e4 ; padding: 2px&quot;&gt;Tablename&lt;/div&gt;&lt;table style=&quot;width: 100% ; font-size: 1em&quot; cellpadding=&quot;2&quot; cellspacing=&quot;0&quot;&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;PK&lt;/td&gt;&lt;td&gt;uniqueId&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;FK1&lt;/td&gt;&lt;td&gt;foreignKey&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;br&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;br&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;&lt;br&gt;&lt;/td&gt;&lt;td&gt;fieldname&lt;br&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;" style="verticalAlign=top;align=left;overflow=fill;html=1;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeColor=#000000;strokeWidth=1;fillColor=#ffffff;fontFamily=Verdana;fontSize=12;fontColor=#000000;" parent="1" vertex="1">
      <mxGeometry x="110" y="680" width="180" height="130" as="geometry"/>
    </mxCell>
    <mxCell id="2ed32ef02a7f4228-13" value="" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=ERoneToMany;startArrow=ERmandOne;labelBackgroundColor=none;fontFamily=Verdana;fontSize=12;align=left;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" parent="1" source="2ed32ef02a7f4228-1" target="2ed32ef02a7f4228-5" edge="1">
      <mxGeometry width="100" height="100" relative="1" as="geometry">
        <mxPoint x="350" y="370" as="sourcePoint"/>
        <mxPoint x="450" y="270" as="targetPoint"/>
      </mxGeometry>
    </mxCell>
  </root>
</mxGraphModel>

```
