# Release Checklist

Use this checklist before publishing a new release.

## Version

- [ ] Update `custom_components/lgess/manifest.json`
- [ ] Update `CHANGELOG.md`
- [ ] Verify `hacs.json`

## Quality

- [ ] All tests pass
- [ ] Ruff reports no issues
- [ ] Hassfest passes successfully
- [ ] Integration starts without warnings
- [ ] Verify diagnostics work
- [ ] Verify translations (de/en)

## Documentation

- [ ] README is up to date
- [ ] Installation instructions verified
- [ ] Screenshots updated (if necessary)

## GitHub

- [ ] Commit all changes
- [ ] Create version tag (`vX.Y.Z`)
- [ ] Create GitHub Release
- [ ] Copy CHANGELOG entry into Release Notes

## Final Verification

- [ ] Install from HACS in a clean Home Assistant instance
- [ ] Verify configuration flow
- [ ] Verify entities are created correctly
- [ ] Verify diagnostics can be downloaded

---

**Only publish the release after every item above has been completed successfully.**
