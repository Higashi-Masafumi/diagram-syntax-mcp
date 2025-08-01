---
title: "Schema Flowchart"
description: "A flowchart diagram showing process flow and decision points"
category: "diagrams"
type: "flowchart"
source_file: "diagrams/schema_decoded.xml"
tags: ["diagram", "drawio", "documentation"]
---

# Schema Flowchart

A flowchart diagram showing process flow and decision points

## XML Source

```xml
<?xml version="1.0" ?>
<mxGraphModel dx="641" dy="1187" grid="0" gridSize="10" guides="1" tooltips="1" connect="1" fold="1" page="1" pageScale="1" pageWidth="826" pageHeight="1169" style="default-style2" math="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <mxCell id="2" value="User" style="swimlane;html=1;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#e0e0e0;horizontalStack=0;resizeParent=1;resizeLast=0;collapsible=1;marginBottom=0;swimlaneFillColor=#ffffff;" parent="1" vertex="1">
      <mxGeometry x="40" y="120" width="140" height="130" as="geometry"/>
    </mxCell>
    <mxCell id="6" value="UserID" style="shape=partialRectangle;top=0;left=0;right=0;bottom=1;html=1;align=left;verticalAlign=top;fillColor=none;spacingLeft=34;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;dropTarget=0;fontStyle=5" parent="2" vertex="1">
      <mxGeometry y="26" width="140" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="7" value="PK" style="shape=partialRectangle;top=0;left=0;bottom=0;html=1;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[];portConstraint=eastwest;part=1;fontStyle=1" parent="6" vertex="1" connectable="0">
      <mxGeometry width="30" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="10" value="AccountName" style="shape=partialRectangle;top=0;left=0;right=0;bottom=0;html=1;align=left;verticalAlign=top;fillColor=none;spacingLeft=34;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;dropTarget=0;" parent="2" vertex="1">
      <mxGeometry y="52" width="140" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="11" value="" style="shape=partialRectangle;top=0;left=0;bottom=0;html=1;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[];portConstraint=eastwest;part=1;" parent="10" vertex="1" connectable="0">
      <mxGeometry width="30" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="14" value="FullName" style="shape=partialRectangle;top=0;left=0;right=0;bottom=0;html=1;align=left;verticalAlign=top;fillColor=none;spacingLeft=34;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;dropTarget=0;" parent="2" vertex="1">
      <mxGeometry y="78" width="140" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="15" value="" style="shape=partialRectangle;top=0;left=0;bottom=0;html=1;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[];portConstraint=eastwest;part=1;" parent="14" vertex="1" connectable="0">
      <mxGeometry width="30" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="12" value="Active" style="shape=partialRectangle;top=0;left=0;right=0;bottom=0;html=1;align=left;verticalAlign=top;fillColor=none;spacingLeft=34;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;dropTarget=0;" parent="2" vertex="1">
      <mxGeometry y="104" width="140" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="13" value="" style="shape=partialRectangle;top=0;left=0;bottom=0;html=1;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[];portConstraint=eastwest;part=1;" parent="12" vertex="1" connectable="0">
      <mxGeometry width="30" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="16" value="UserUserRole" style="swimlane;html=1;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#e0e0e0;horizontalStack=0;resizeParent=1;resizeLast=0;collapsible=1;marginBottom=0;swimlaneFillColor=#ffffff;" parent="1" vertex="1">
      <mxGeometry x="240" y="94" width="160" height="156" as="geometry"/>
    </mxCell>
    <mxCell id="34" value="UserID" style="shape=partialRectangle;top=0;left=0;right=0;bottom=0;html=1;align=left;verticalAlign=top;fillColor=none;spacingLeft=60;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;dropTarget=0;fontStyle=5" parent="16" vertex="1">
      <mxGeometry y="26" width="160" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="35" value="PK,FK1" style="shape=partialRectangle;top=0;left=0;bottom=0;html=1;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[];portConstraint=eastwest;part=1;fontStyle=1" parent="34" vertex="1" connectable="0">
      <mxGeometry width="56" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="17" value="UserRoleID" style="shape=partialRectangle;top=0;left=0;right=0;bottom=1;html=1;align=left;verticalAlign=top;fillColor=none;spacingLeft=60;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;dropTarget=0;fontStyle=5" parent="16" vertex="1">
      <mxGeometry y="52" width="160" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="18" value="PK,FK2" style="shape=partialRectangle;top=0;left=0;bottom=0;html=1;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[];portConstraint=eastwest;part=1;fontStyle=1" parent="17" vertex="1" connectable="0">
      <mxGeometry width="56" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="19" value="BeginDate" style="shape=partialRectangle;top=0;left=0;right=0;bottom=0;html=1;align=left;verticalAlign=top;fillColor=none;spacingLeft=60;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;dropTarget=0;" parent="16" vertex="1">
      <mxGeometry y="78" width="160" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="20" value="" style="shape=partialRectangle;top=0;left=0;bottom=0;html=1;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[];portConstraint=eastwest;part=1;" parent="19" vertex="1" connectable="0">
      <mxGeometry width="56" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="21" value="EndDate" style="shape=partialRectangle;top=0;left=0;right=0;bottom=0;html=1;align=left;verticalAlign=top;fillColor=none;spacingLeft=60;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;dropTarget=0;" parent="16" vertex="1">
      <mxGeometry y="104" width="160" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="22" value="" style="shape=partialRectangle;top=0;left=0;bottom=0;html=1;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[];portConstraint=eastwest;part=1;" parent="21" vertex="1" connectable="0">
      <mxGeometry width="56" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="23" value="CreatedDate" style="shape=partialRectangle;top=0;left=0;right=0;bottom=0;html=1;align=left;verticalAlign=top;fillColor=none;spacingLeft=60;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;dropTarget=0;" parent="16" vertex="1">
      <mxGeometry y="130" width="160" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="24" value="" style="shape=partialRectangle;top=0;left=0;bottom=0;html=1;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[];portConstraint=eastwest;part=1;" parent="23" vertex="1" connectable="0">
      <mxGeometry width="56" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="25" value="UserRole" style="swimlane;html=1;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#e0e0e0;horizontalStack=0;resizeParent=1;resizeLast=0;collapsible=1;marginBottom=0;swimlaneFillColor=#ffffff;" parent="1" vertex="1">
      <mxGeometry x="460" y="120" width="140" height="130" as="geometry"/>
    </mxCell>
    <mxCell id="26" value="UserRoleID" style="shape=partialRectangle;top=0;left=0;right=0;bottom=1;html=1;align=left;verticalAlign=top;fillColor=none;spacingLeft=34;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;dropTarget=0;fontStyle=5" parent="25" vertex="1">
      <mxGeometry y="26" width="140" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="27" value="PK" style="shape=partialRectangle;top=0;left=0;bottom=0;html=1;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[];portConstraint=eastwest;part=1;fontStyle=1" parent="26" vertex="1" connectable="0">
      <mxGeometry width="30" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="28" value="UserRoleName" style="shape=partialRectangle;top=0;left=0;right=0;bottom=0;html=1;align=left;verticalAlign=top;fillColor=none;spacingLeft=34;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;dropTarget=0;" parent="25" vertex="1">
      <mxGeometry y="52" width="140" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="29" value="" style="shape=partialRectangle;top=0;left=0;bottom=0;html=1;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[];portConstraint=eastwest;part=1;" parent="28" vertex="1" connectable="0">
      <mxGeometry width="30" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="32" value="Description" style="shape=partialRectangle;top=0;left=0;right=0;bottom=0;html=1;align=left;verticalAlign=top;fillColor=none;spacingLeft=34;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;dropTarget=0;" parent="25" vertex="1">
      <mxGeometry y="78" width="140" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="33" value="" style="shape=partialRectangle;top=0;left=0;bottom=0;html=1;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[];portConstraint=eastwest;part=1;" parent="32" vertex="1" connectable="0">
      <mxGeometry width="30" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="30" value="Active" style="shape=partialRectangle;top=0;left=0;right=0;bottom=0;html=1;align=left;verticalAlign=top;fillColor=none;spacingLeft=34;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;dropTarget=0;" parent="25" vertex="1">
      <mxGeometry y="104" width="140" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="31" value="" style="shape=partialRectangle;top=0;left=0;bottom=0;html=1;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;whiteSpace=wrap;overflow=hidden;rotatable=0;points=[];portConstraint=eastwest;part=1;" parent="30" vertex="1" connectable="0">
      <mxGeometry width="30" height="26" as="geometry"/>
    </mxCell>
    <mxCell id="36" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;" parent="1" source="16" target="2" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="210" y="200"/>
          <mxPoint x="210" y="200"/>
        </Array>
      </mxGeometry>
    </mxCell>
    <mxCell id="37" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;" parent="1" source="16" target="25" edge="1">
      <mxGeometry relative="1" as="geometry">
        <Array as="points">
          <mxPoint x="430" y="200"/>
          <mxPoint x="430" y="200"/>
        </Array>
      </mxGeometry>
    </mxCell>
  </root>
</mxGraphModel>

```
