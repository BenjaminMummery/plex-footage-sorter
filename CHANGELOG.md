# CHANGELOG

## v4.5.2 (2024-07-15)

### Fix

* fix: ignore diplicate files as marked by subscript version numbers. ([`ed45a28`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/ed45a28f1869f3516574f9ed7c8df50b35e67869))

### Unknown

* Merge pull request #39 from BenjaminMummery/fix/ignore-subscripted-duplicate-files

fix: ignore diplicate files as marked by subscript version numbers. ([`5126962`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/5126962d7fbcbd44de7dcc2f9a7a4bf7288c0e4f))

## v4.5.1 (2024-07-15)

### Fix

* fix: handle m-dashes between days and hours. ([`f59f215`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/f59f215bfec7ee79d7eff609b2efe14034a93bbc))

### Test

* test: add test to reproduce m-dash bug. ([`0e1da08`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/0e1da080fc243d2347423236242307629cb20937))

### Unknown

* Merge pull request #38 from BenjaminMummery/fix/m-dashes

Fix: m-dashes between days and hours cause files to be ignored. ([`f4e8e85`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/f4e8e8576d2f868718a7c3483c0f3eadf514aa12))

## v4.5.0 (2024-07-15)

### Chore

* chore: use backwards-compatible typehints. ([`0b35d19`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/0b35d19393fef8ef8d4dc19b6c696032602264d1))

### Feature

* feat: handle a wider range of name formats.

We previously supported &#39;YYYYMMDD_HHMMSS&#39;. We now additionally support &#39;YYYYMMDD_HHMMSSmmm&#39;, &#39;YYYYMMDD_HHMM&#39;, and variants with - betweent he componenets. ([`d9d1e90`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/d9d1e90138083076fe0f8d6790c1c91b8095049b))

### Test

* test: add tests for multiple file naming formats. ([`ce4cac7`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/ce4cac7453911bcd8c0aba3df7818bdbc3af4f92))

### Unknown

* Merge pull request #37 from BenjaminMummery/feat/more-flexible-date-parsing

Feat: more flexible date parsing ([`c87f8e2`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/c87f8e2ea4f0d400e05454904965cd65499c4afb))

## v4.4.0 (2024-01-09)

### Chore

* chore: remove extranious print. ([`45a70c1`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/45a70c138973470286e1afade76de44570e3c741))

### Feature

* feat: handle multiple wildcards. ([`34f4877`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/34f48777c57731c7c40c3ea1cd3f155855e7c455))

* feat: throw an exception for mismatching wildcards. ([`bc34a0f`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/bc34a0f0e3559b5ddbb6642c4a28ec0ebf7fe95b))

* feat: remove regex arg. ([`1ad512d`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/1ad512d68e000d507205d32155f553dd7152ce7a))

* feat: handle ? wildcards. ([`4b72a3d`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/4b72a3db54a5ed603b7d0b5730e0b50ccf332c0c))

* feat: rename with single * wildcard. ([`b83efb2`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/b83efb29da0710d42d116f512e23a60602cacc6e))

* feat: handle args to rename. ([`cd1d40c`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/cd1d40c45e619f7e903e21fcdf41b41bbd2b90a8))

* feat: pass regex arg to rename. ([`5b1681f`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/5b1681f74ebdab9dccecd4415fae1984bf298f19))

* feat: implement argument passing. ([`7cb557f`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/7cb557fc1240f87955415e31415c1d7eac65873b))

* feat: placeholder rename method. ([`226bdfe`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/226bdfe67cfb2843f2ec27b83ba1438265f27a96))

### Refactor

* refactor: separate tests by wildcard. ([`c664c44`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/c664c44a4e79a224e1f5fd325f3c4ff1c1a1427f))

### Test

* test: add test for multiple wildcards. ([`a89c6dc`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/a89c6dc4f2e61f12de7506004795560deae6b28c))

* test: add test for mismatching wildcards. ([`b653d89`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/b653d89e15b30571b762a07c4cbfcbaabb0d220c))

* test: add test for unsupported glob wildcards. ([`527a14e`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/527a14ef820efe93600312a988041ad6c25529f5))

* test: add tests for combinations of multiple files. ([`94ead0d`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/94ead0d49582d627a543c07840e3e495b4d5f997))

* test: add test for ? wildcard. ([`37e32ed`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/37e32ede1ca036997bfde2124b1d9d14892f586c))

* test: add test for renaming single file. ([`c86fab3`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/c86fab34bdc9c8a59b24cdb40519c57ba7fab4df))

* test: add test for no matching files. ([`7729a1b`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/7729a1bfd126943b102581d7ce341a4d3263734c))

* test: add test for null case - no files. ([`ec89fc7`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/ec89fc73198fe000aca1cd72a81472db15c6d41f))

* test: add test for directory logic. ([`69eccda`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/69eccda697002197a9a1792775cc2f3fa9ea16f9))

* test: add test for missing rename args. ([`ba25dda`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/ba25dda686ddbc7ef2ef822127145f08e6287ab4))

* test: add test for passing regex argument to rename. ([`205c273`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/205c27342ea18abbd10494cef8d6b537de854c7e))

* test: add test for arg passing to rename. ([`64c55dc`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/64c55dc6bf99f134fed5e539873f02535766c4a8))

* test: add asserts that rename is not called when invoking other commands. ([`759ea16`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/759ea16850826cb7c203c7ace242e88e51c99843))

### Unknown

* Merge pull request #32 from BenjaminMummery/feat/renamer

feat: renamer ([`c11ca7b`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/c11ca7b75c6e02ef54ece59a2f5ced5dbedf0fbf))

## v4.3.1 (2023-12-05)

### Fix

* fix: handle preexisting season subdir. ([`22713d4`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/22713d4985ed5a56be922d8a6152fa1c7f2e0e23))

### Style

* style: fix style ([`896de4c`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/896de4cce19e4485016b3716d5fd62d8fdd04da8))

### Unknown

* Merge pull request #31 from BenjaminMummery/fix-allow-preexisting-subdirs

fix: handle preexisting season subdir. ([`60a2aba`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/60a2abaf6839b0a735b7f00e2e4d3ac646b274c8))

## v4.3.0 (2023-12-05)

### Documentation

* docs: update readme. ([`f771487`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/f7714875c895f2f070d1d7e28229a31449041881))

* docs: update docs ([`fd0dd04`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/fd0dd0414838f66cb96688eeabaeef313a3eb7ed))

### Feature

* feat: handle netflix style series structures. ([`7314457`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/7314457aed71f1ed4597d61110b38354360ee223))

### Refactor

* refactor: adjust tests for multiple subdir formats. ([`c756445`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/c7564459cfd06b79421fb81970c80139966d31e1))

### Test

* test: add test for non-matching subdir names. ([`49eac5d`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/49eac5d25972dc9a67bc60c56030fdcaeeced522))

* test: add tests for netflix-pattern directory structures. ([`1f664e6`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/1f664e67a3e712fc83cf5226acb781b320bb2c7e))

## v4.2.0 (2023-12-05)

### Chore

* chore: bump pytest version. ([`27f5f01`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/27f5f019b9d678d36984d854b6c7410a1e872c6d))

### Ci

* ci: enable self-hosted runner. ([`2ba284b`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/2ba284bfae446ad11ff531143819107487a4b20b))

### Documentation

* docs: fix typo in README.

&#39;Season011&#39; should actually be &#39;Season01&#39;. ([`1df53a0`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/1df53a010cc0d054e5b2c2559d84fc0e4b4aad55))

### Feature

* feat: delete empty subdirs when done. ([`05516b0`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/05516b05fbeed8329eb4e22259fd91a34ed2ded2))

* feat: implement custom directory arg. ([`4f8978b`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/4f8978b8c5977468f30e677ed0b6c7192675a4ff))

### Fix

* fix: correct &#39;title&#39; arg for wrong command in test. ([`75eabd0`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/75eabd0e76a88c86c12ba2ca7ee9f75bc096ecb6))

### Style

* style: apply style rules to actions yaml. ([`0c83cd8`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/0c83cd82db7f2d32c3bedab1b26ced9f3f643c48))

### Test

* test: update tests for subdir structure. ([`9f6da8b`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/9f6da8b334c73333c508c403f0f5141c223257d2))

* test: add tests for custom directory argument. ([`a9b2d7d`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/a9b2d7d7434f9c06824d6df5ff47c3b760b53476))

### Unknown

* Revert &#34;ci: enable self-hosted runner.&#34;

This reverts commit d9a43b399ca50a80234c7fcd1214bbba68f6b317. ([`fce7e03`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/fce7e033522b65979f4e7a40161c9b1ea1481dc7))

## v4.1.0 (2023-12-04)

### Feature

* feat: implement &#39;--version&#39; command. ([`7750506`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/775050652e5ed49df4e8f3ffbfdf76c085900e45))

### Test

* test: add test for ([`61de859`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/61de85966f8de909f1ed08be37a15f5e40a84a73))

## v4.0.0 (2023-12-04)

### Chore

* chore: add template movpilot sorter script. ([`a32df7f`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/a32df7f64a81f030de6de4330bcd57b7a9628847))

### Ci

* ci: only enforce integration test coverage ([`a5da104`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/a5da104c5ba3488fe8cb3083d2bd4a1da5a6b3de))

* ci: separate unit and integration test runs. ([`ab7b3c3`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/ab7b3c38d02401f632768dbe8ea53ebf417de8e6))

* ci: enforce 100% coverage? ([`8890081`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/8890081cd61404fbf7f59c786e25033eeff65417))

* ci: nope, that didn&#39;t work, scrapping reporting unit test coverage. ([`9109d7d`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/9109d7d188feb3f88fe0413e651508e9e76b8525))

* ci: report unit test coverage. ([`22dd8f0`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/22dd8f0e4e111fe94566ceeb43c2b868ec1983dc))

### Documentation

* docs: update readme. ([`7a99b4c`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/7a99b4ccb26164793ca921d4e0ab83d53ee4abc4))

* docs: fix type in docstring. ([`67ca43e`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/67ca43e1b994e8ac3666107bd9b50ca806848851))

### Feature

* feat: handle supplemental non-episode files. ([`65ee382`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/65ee3822eed7d604a77196047e460b0abbfdaf50))

* feat: handle supplemental non-episode files. ([`c65da4a`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/c65da4a8e86f32114bfec87e68137e6ce48b7956))

* feat: create correct subdirs for missing seasons. ([`bdf1331`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/bdf1331bab0011dd35839eb33b16045eb5969baa))

* feat: remove underscores from episode titles. ([`c541e9d`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/c541e9d164915eabece1526ac5b056d178b48dbb))

* feat: implement movpilot file sorting, ([`aeb42ec`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/aeb42ec699da751fe2478aed4e7087acc8c772e0))

* feat: call movpilot sorter from entry. ([`ab7f11e`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/ab7f11e6075fbe1b04d73f0b00ce6057fe8cb295))

* feat: minimal movpilot implementation. ([`7afe9b2`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/7afe9b2bdfcffbf4647a32e75ec8a1f2efd684c8))

### Fix

* fix: integration tests need to patch srgv. ([`ca6ecd1`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/ca6ecd1899c0b69c74eb788ed160ff6c5c8759a2))

### Style

* style: remove unused local variable. ([`b6f815f`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/b6f815fc39ff4521cc5adfbd2053ef3588114fce))

### Test

* test: add test for supplemental files. ([`bf2ce98`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/bf2ce98a992f52f4bffe861324b7f4b5f12eb099))

* test: add test for episodes outside of season structure. ([`ae6f7c9`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/ae6f7c9a471d1a54e23ba50941a84d1461447839))

* test: add tests for multiple series and misfiled episodes. ([`fdbbdd9`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/fdbbdd9dbbe7325a95188207ea3027b865cb559f))

* test: add test for multiple amazon-style files. ([`12d0c5e`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/12d0c5e4ddaa0eafa8a29df1e042caca86b7f6ea))

* test: add test for renaming single movpilot file. ([`e45401a`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/e45401ab6bc0fd4f59186a5f19bc2764f57c0eac))

* test: add unit test for calling movpilot sorter. ([`70471ba`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/70471bafdc8f0017d90941ecc6aae288d1f8ae10))

* test: add unit tests for entry. ([`2f68681`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/2f68681467e4df38963019c702e7eadb0dbc4864))

* test: add tests for minimal movpilot sorter. ([`11a37f2`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/11a37f21564f90b58a6cfd5e1700b9101d57e691))

* test: expaded system tests. ([`06e7c8a`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/06e7c8ab5b52c2d5f80a2d3e3edfb8412bbcf710))

### Unknown

* Merge pull request #25 from BenjaminMummery/21-rename-movpilot-series-downloads

feat: rename movpilot series downloads ([`94b076e`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/94b076e0332329f329d595c4aa4d78f91ee82e21))

* Update python-publish.yml ([`48ca88e`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/48ca88e308897e01f4d74c46376a023587f5fcfd))

* Update coverage.yml ([`16948fc`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/16948fca2d3d7408631d4865eee6fa9f04249490))

* Update coverage.yml ([`0e75427`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/0e754270cb689f4daa17b15f6bca86b975312f12))

* Merge branch &#39;main&#39; into 21-rename-movpilot-series-downloads ([`b0a559e`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/b0a559e5337968f7bb04994be2f44f06b60dedad))

## v3.0.0 (2023-11-28)

### Breaking

* feat: switch to CLI subcommands.

BREAKING CHANGE: `date-based` must now be specified when calling `plex-footage-sorter` in order to access the previous default behaviour. ([`5baaacf`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/5baaacf497cef42e624c1c5ed3fbe9a289764603))

* feat: switch to CLI subcommands.

BREAKING CHANGE: `date-based` must now be specified when calling `plex-footage-sorter` in order to access the previous default behaviour. ([`2910b60`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/2910b60d9ace6ff6d6bbb9b9729c6ca87bda240f))

### Chore

* chore: fix typo in README. ([`67d5b6c`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/67d5b6ca7fdd1706ac42371c5809405fb80718b8))

* chore: bump version number. ([`3a9fcd1`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/3a9fcd16cb8048893f5e15e14e18150a7bfed027))

* chore: fix typo in README. ([`8839a6e`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/8839a6e664345936405d339ae53d79f42da23a6b))

* chore: bump version number. ([`e810c3a`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/e810c3af020b6e8b289bff87b509e27bad70ab7d))

### Documentation

* docs: update readme. ([`5d92a76`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/5d92a76ffaf9c77f95881c240f9eebe0f769c1bd))

### Refactor

* refactor: move date-based sorting to its own source file. ([`97d1a13`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/97d1a1349f06c571df7e14e47b3971ea8a66bd81))

* refactor: move date-based sorting to its own source file. ([`decdf1d`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/decdf1db8ed4d9d2b9c470696b08ada7691d7b70))

### Test

* test: add tests for change to subcommand cli. ([`60a698c`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/60a698c769585c09e7716ce01c3ee9abcf593609))

* test: adjust test strategy towards unit testing. ([`e7d7ab2`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/e7d7ab277d7333169547f5f6388cf8af8940dbc5))

* test: add tests for change to subcommand cli. ([`e70dfd9`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/e70dfd9afd1538f1585ee00f2e73b5ad58a7a273))

## v2.0.0 (2023-11-28)

### Unknown

* Chore!: Rename (#20)

* chore!: Package rename.

* docs: update README. ([`4eb396e`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/4eb396eaee0f33aa22bff668eb76fffd06b45ade))

## v1.2.0 (2023-11-27)

### Feature

* feat: add recursive option (#19)

* test: add test for file in subdir.

* feat: rename files recursively.

* test: add tests for improper use of recursion ([`cc94f87`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/cc94f87536d1e14a083d18968b25b351112373d6))

## v1.1.1 (2023-11-25)

### Fix

* fix: correct version numbering

Fixes a bug where build versions would default to 0.0.0 ([`c25b55b`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/c25b55baf8931586cb8353d0db461ae14e99c720))

### Unknown

* Merge pull request #13 from BenjaminMummery/fix/build-version-numbering

fix: correct version numbering ([`ff7861e`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/ff7861ede7bb901de46e34b1dba726f0ebaf2409))

## v1.1.0 (2023-11-25)

### Feature

* feat: report file discovery. ([`7bd5e30`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/7bd5e307dc8fae837db82897b12baad685d90ebd))

### Test

* test: update tests for more verbose output. ([`400ba18`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/400ba18c1240966cce90ed5dc4ab48bcfae9ad6f))

### Unknown

* Merge pull request #12 from BenjaminMummery/feat/report-file-discovery

feat: report file discovery ([`f78deb1`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/f78deb19ad0a75823f0829ffb00424cd4bf3583a))

* Feat: report no changes (#10)

* chore: bump version.

* feat: report no changes. ([`191f4b5`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/191f4b5bb7ec48c023d9128009dffdda27175d87))

* Update deploy.yml ([`2a6bfc4`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/2a6bfc4476dddb6fceff5afebaecba990118da71))

## v1.0.1 (2023-11-24)

### Breaking

* feat!: simple mapping implementation (#6)

* ci: configure semantic release.

* test: add test for single file renaming.

* test: add test for renaming multiple files.

* feat: implement flat dir renaming.

* style: reformat makefile.

* test: add system tests for flat folder.

* chore: add build dir to gitignore.

* fix: correct typo in pyproject.

* test: add test for non-matching files.

* feat: handle non-matching files.

* test: add tests for custom naming.

* feat: add custom naming. ([`0249f5d`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/0249f5d0bf58e0f1b3b8201a885d99c5850ac1ca))

### Ci

* ci: semantic-release setup. (#4) ([`de77aae`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/de77aaeb2f3d52653a2af4b5e91ae77bd0442e44))

* ci: automated release? ([`a1f20e1`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/a1f20e12b076c7ebe60ab3d94303ecd274994695))

* ci: remove build step. ([`e008689`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/e008689267a51ae4085199cc41ad9ac310427274))

* ci: don&#39;t build wheel to test install. ([`7433a17`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/7433a173d2f135c4f47386e3c992ca82df64510d))

* ci: build wheel for testing. ([`648af2f`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/648af2f83a97c79f934f2b660ed529fb9f39a094))

* ci: action permissions? ([`42b623e`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/42b623e873bcde5a3e8273555d07e721755469d9))

* ci: add makefile. ([`ca8d6b4`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/ca8d6b4d96bf00e1ebf1741b9bbb777511dc0afe))

* ci: initial testing setup. ([`8eae69a`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/8eae69ac2b16ccca0aaf666265fb40f3da878db1))

* ci: add pre-commit config. ([`6fe2710`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/6fe271038d291df6c0b6b480cf89aa80db5af3a8))

### Documentation

* docs: update README.md ([`d05926e`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/d05926efc20051fd88a88b6896af6794818b30fb))

### Fix

* fix: point ci to correct tests. ([`d1381ce`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/d1381cef53e7b705048aa0570220c5a9fd495155))

### Test

* test: add placeholder unit test. ([`1eae0db`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/1eae0db6bd03b58124fe7ef31d986ea31a8e1f69))

* test: add system tests. ([`767baac`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/767baac1fac5efc6957cf9d6b66a61d1f6de48fb))

### Unknown

* Feat: report changed files (#9)

* test: add test for reporting change files.

* feat: report changed files. ([`a848d96`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/a848d9611492f7eb27c700258cb1dc6514584212))

* Create python-publish.yml (#8) ([`12a18da`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/12a18dae8eab012c1a52f2858ff25ae8b0c91638))

* V1.0.0 (#7)

* ci: exclude changelog.

* docs: update changelog.

* docs: update changelog.

* docs: update changelog.

* ci: update release process.

* docs: update changelog.

* build: 1.0.0

Automatically generated by python-semantic-release

---------

Co-authored-by: semantic-release &lt;semantic-release&gt; ([`de224b0`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/de224b09889818f6fa065f86aaee92cf6f796186))

* Merge pull request #3 from BenjaminMummery/2-set-up-ci

CI: 2 set up ci ([`ebba57a`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/ebba57afa61a2d3dec2146b3ccb85ab8b05d1cae))

* Initial commit ([`ac38349`](https://github.com/BenjaminMummery/plex-footage-sorter/commit/ac3834951db1ea32b8545b8cf47a0b148b795794))
