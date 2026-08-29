# API Reference

::: mudu
    options:
      show_source: false
      members: true
      show_signature_annotations: true
      filters:
        - "!^_"          # start clean: hide everything underscore-prefixed
        - "^_[^_]"       # re-show single-underscore names (e.g. _UnitType, _DimensionType)
        - "^__init__$"   # re-show __init__ specifically, but no other dunders

!!! note
    `define_unit`, `register_conversion`, `audit_units`, `Linear`, and `Affine` are the supported public extension surface as of this release. See [Usage Guide](usage.md) and [What's Changed](whats_changed.md). Members prefixed with a single underscore (e.g. `_UnitType`, `_DimensionType`) are documented here for completeness but are internal; use them directly only when defining an entirely new quantity with no existing dimension to attach to.