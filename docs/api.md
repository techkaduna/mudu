# API Reference

::: mudu
    options:
      show_source: false
      members: true
      show_signature_annotations: true
      show_private_members: true
      show_special_members: true

!!! note
    `define_unit`, `register_conversion`, `audit_units`, `Linear`, and `Affine` are the supported public extension surface as of this release. See [Usage Guide](usage.md) and [What's Changed](whats_changed.md). Members prefixed with a single underscore (e.g. `_UnitType`, `_DimensionType`) are documented here for completeness but are internal; use them directly only when defining an entirely new quantity with no existing dimension to attach to.