<%inherit file="layout.mako"/>
<div class="content">
  <p class="lead">Welcome to <span class="font-normal">Drumio</span><br><span class="font-normal">an AI based source separation engine</span>.</p>

  <form action="/store_track" method="post" accept-charset="utf-8" enctype="multipart/form-data">
    <div class="form-group">
      <label>Upload a track</label> <br/>
      <input type="file" class="form-control-file" id="track" name="track"> <br/>
      <button type="submit" class="btn btn-primary mb-2">Upload</button>
    </div>
  </form>
</div>
